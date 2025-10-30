#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

try:
    import pikepdf  # optional fallback
    HAVE_PIKEPDF = True
except Exception:
    HAVE_PIKEPDF = False


def human(n):
    for unit in ["B","KB","MB","GB"]:
        if n < 1024.0:
            return f"{n:.2f} {unit}"
        n /= 1024.0
    return f"{n:.2f} TB"


def detect_gs():
    """
    Try to find Ghostscript executable across platforms.
    Returns executable name or None if not found.
    """
    candidates = ["gs", "gswin64c", "gswin32c"]
    for c in candidates:
        p = shutil.which(c)
        if p:
            return p
    return None


def run_gs(in_pdf, out_pdf, dpi=150, jpeg_q=85, force_jpeg=False, keep_meta=False):
    """
    Run Ghostscript with fine-grained image downsample & JPEG quality control.
    """
    gs = detect_gs()
    if not gs:
        raise RuntimeError("Ghostscript not found. Please install Ghostscript.")

    args = [
        gs,
        "-dQUIET", "-dBATCH", "-dNOPAUSE", "-dSAFER",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.6",

        # Keep vector/text as is
        "-dColorConversionStrategy=/LeaveColorUnchanged",
        "-dAutoRotatePages=/None",

        # Fonts & structure
        "-dCompressFonts=true",
        "-dSubsetFonts=true",
        "-dDetectDuplicateImages=true",

        # Metadata handling
    ]
    if not keep_meta:
        args += ["-dPreserveMarkedContent=false", "-dPreserveCopyPage=false"]

    # Downsample settings (bicubic gives good quality/size balance)
    for space in ["Color", "Gray", "Mono"]:
        args += [f"-dDownsample{space}Images=true"]
        args += [f"-d{space}ImageDownsampleType=/Bicubic"]
        args += [f"-d{space}ImageResolution={dpi}"]
        args += [f"-dEncode{space}Images=true"]

        if force_jpeg or space in ("Color", "Gray"):
            args += [f"-d{space}ImageFilter=/DCTEncode"]  # JPEG
        else:
            # Let GS choose for mono
            args += [f"-d{space}ImageAutoFilterStrategy=/Quality"]

    # JPEG quality (affects DCTEncode)
    # Ghostscript uses -dJPEGQ for global quality
    args += [f"-dJPEGQ={jpeg_q}"]

    args += [
        f"-sOutputFile={out_pdf}",
        str(in_pdf)
    ]

    res = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0 or (not Path(out_pdf).exists()):
        raise RuntimeError(
            f"Ghostscript failed (code {res.returncode}). "
            f"stderr: {res.stderr.decode(errors='ignore')}"
        )


def quick_optimize_with_pikepdf(in_pdf, out_pdf):
    """
    If GS is unavailable, at least optimize streams & object usage with pikepdf.
    This rarely achieves 1/10 by itself but can shave off some MB.
    """
    if not HAVE_PIKEPDF:
        shutil.copy2(in_pdf, out_pdf)
        return

    with pikepdf.open(in_pdf) as pdf:
        # Remove unused objects, recompress streams where possible
        pdf.save(
            out_pdf,
            linearize=True,
            fix_metadata=True,
            compress_streams=True,
            object_stream_mode=pikepdf.ObjectStreamMode.generate,
            preserve_pdfa=False,
        )


def compress_pdf_smart(
    in_pdf: Path,
    out_pdf: Path,
    target_ratio: float = 0.10,
    max_dpi: int = 300,
    min_dpi: int = 96,
    q_max: int = 95,
    q_min: int = 60,
    steps: int = 6,
    force_jpeg: bool = False,
    keep_meta: bool = False,
):
    """
    Try multiple (dpi, jpeg_q) combos until output <= target size.
    If none hit target, keep smallest successful result.
    """
    in_size = in_pdf.stat().st_size
    target_size = int(in_size * target_ratio)

    if in_size == 0:
        raise ValueError("Input file size is 0.")

    # Prepare candidate DPIs descending (e.g., 300 -> ... -> 96)
    if steps < 2:
        steps = 2
    dpi_candidates = sorted(
        {int(min_dpi + (max_dpi - min_dpi) * (i / (steps - 1))) for i in range(steps)},
        reverse=True,
    )
    # ensure boundaries included
    if max_dpi not in dpi_candidates:
        dpi_candidates.insert(0, max_dpi)
    if min_dpi not in dpi_candidates:
        dpi_candidates.append(min_dpi)

    # JPEG quality candidates (high -> low)
    q_candidates = list(range(q_max, q_min - 1, -5))

    best_path = None
    best_size = None

    with tempfile.TemporaryDirectory() as td:
        tmp_out = Path(td) / "out.pdf"

        try:
            # quick prepass: just recompress default (often gets 20~60%)
            run_gs(in_pdf, tmp_out, dpi=max_dpi, jpeg_q=min(q_max, 90),
                   force_jpeg=force_jpeg, keep_meta=keep_meta)
            cur_size = tmp_out.stat().st_size
            best_path = tmp_out
            best_size = cur_size

            if cur_size <= target_size:
                shutil.copy2(tmp_out, out_pdf)
                return True, in_size, cur_size, target_size

        except Exception:
            # If GS unavailable, try pikepdf minimal optimization
            quick_tmp = Path(td) / "quick.pdf"
            quick_optimize_with_pikepdf(in_pdf, quick_tmp)
            cur_size = quick_tmp.stat().st_size
            best_path = quick_tmp
            best_size = cur_size
            if cur_size <= target_size:
                shutil.copy2(quick_tmp, out_pdf)
                return True, in_size, cur_size, target_size

        # Full search
        for dpi in dpi_candidates:
            for q in q_candidates:
                try:
                    run_gs(in_pdf, tmp_out, dpi=dpi, jpeg_q=q,
                           force_jpeg=force_jpeg, keep_meta=keep_meta)
                    cur_size = tmp_out.stat().st_size

                    # Update best
                    if (best_size is None) or (cur_size < best_size):
                        shutil.copy2(tmp_out, out_pdf)
                        best_path = out_pdf
                        best_size = cur_size

                    if cur_size <= target_size:
                        shutil.copy2(tmp_out, out_pdf)
                        return True, in_size, cur_size, target_size
                except Exception:
                    # try next combo
                    continue

        # No combo hit target; output best found
        if best_path is not None:
            if best_path != out_pdf:
                shutil.copy2(best_path, out_pdf)
            return False, in_size, best_size, target_size

        # As absolute fallback
        shutil.copy2(in_pdf, out_pdf)
        return False, in_size, in_size, target_size


def is_pdf(p: Path):
    return p.suffix.lower() == ".pdf"


def gather_inputs(path: Path):
    if path.is_dir():
        return [p for p in path.glob("**/*.pdf")]
    return [path] if is_pdf(path) else []


def main():
    ap = argparse.ArgumentParser(description="PDF Compressor (quality-preserving, image-focused)")
    ap.add_argument("input", type=str, help="Input PDF file or directory")
    ap.add_argument("-o", "--output", type=str, required=True,
                    help="Output file (for single input) or directory (for batch)")
    ap.add_argument("-r", "--target-ratio", type=float, default=0.10,
                    help="Target size ratio (0.10 means 10%% of original)")
    ap.add_argument("--min-dpi", type=int, default=96)
    ap.add_argument("--max-dpi", type=int, default=300)
    ap.add_argument("--q-min", type=int, default=60)
    ap.add_argument("--q-max", type=int, default=95)
    ap.add_argument("--steps", type=int, default=6, help="How many DPI steps to try between min/max")
    ap.add_argument("--force-jpeg", action="store_true", help="Force JPEG for images")
    ap.add_argument("--keep-meta", action="store_true", help="Keep metadata instead of stripping")

    args = ap.parse_args()
    in_path = Path(args.input)
    outs = Path(args.output)

    inputs = gather_inputs(in_path)
    if not inputs:
        raise SystemExit("No PDF found.")

    batch = len(inputs) > 1 or in_path.is_dir()
    if batch:
        outs.mkdir(parents=True, exist_ok=True)

    for src in inputs:
        dst = outs / src.name if batch else Path(args.output)
        ok, in_size, out_size, target_size = compress_pdf_smart(
            src, dst,
            target_ratio=args.target_ratio,
            max_dpi=args.max_dpi,
            min_dpi=args.min_dpi,
            q_max=args.q_max,
            q_min=args.q_min,
            steps=args.steps,
            force_jpeg=args.force_jpeg,
            keep_meta=args.keep_meta,
        )
        status = "✅ HIT" if ok else "⚠️ CLOSE"
        print(f"{status}  {src.name}: {human(in_size)} → {human(out_size)}  (target ≤ {human(target_size)})  → {dst}")

if __name__ == "__main__":
    main()

#$ python pdf_shrink.py ./in_dir -o ./out_dir -r 0.10