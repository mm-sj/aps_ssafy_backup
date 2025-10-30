#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
이미지 기반 PDF 일괄 압축 (Poppler 불필요)
in_dir 폴더 안의 모든 PDF → JPEG 재압축 → out_dir 폴더에 저장
"""

import fitz  # PyMuPDF
from fpdf import FPDF
from PIL import Image
import tempfile, os
from pathlib import Path

def compress_image_pdf(in_pdf, out_pdf, zoom=1.0, quality=50):
    """하나의 PDF 파일을 이미지 기반으로 압축"""
    doc = fitz.open(in_pdf)
    in_size = Path(in_pdf).stat().st_size

    with tempfile.TemporaryDirectory() as td:
        img_paths = []
        for i, page in enumerate(doc):
            pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
            img_path = os.path.join(td, f"page_{i}.jpg")
            pix.save(img_path)
            im = Image.open(img_path)
            im.save(img_path, "JPEG", quality=quality)
            img_paths.append(img_path)

        pdf = FPDF(unit="pt", format=[pix.width, pix.height])
        for img in img_paths:
            pdf.add_page()
            pdf.image(img, 0, 0)
        pdf.output(out_pdf, "F")

    out_size = Path(out_pdf).stat().st_size
    ratio = (out_size / in_size) * 100
    print(f"✅ {Path(in_pdf).name}: {in_size/1024/1024:.2f} MB → {out_size/1024/1024:.2f} MB ({ratio:.1f}%)")

# -------------------------------
# 폴더 내 모든 PDF 일괄 처리 부분
# -------------------------------

in_dir = Path("in_dir")     # 입력 폴더
out_dir = Path("out_dir")   # 출력 폴더
out_dir.mkdir(exist_ok=True)

for pdf_path in in_dir.glob("*.pdf"):
    out_path = out_dir / pdf_path.name
    compress_image_pdf(pdf_path, out_path, zoom=0.6, quality=30)


print("\n🎉 모든 PDF 압축 완료!")
