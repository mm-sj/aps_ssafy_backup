from PIL import Image
import os

path = r"C:\Users\SSAFY\Desktop\오창\ai\pdf저장\images"
files = sorted([f for f in os.listdir(path) if f.endswith(".jpg")])
images = [Image.open(os.path.join(path, f)).convert("RGB") for f in files]
images[0].save(os.path.join(path, "ebook.pdf"), save_all=True, append_images=images[1:])
print("✅ ebook.pdf 생성 완료")
