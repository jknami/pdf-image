import fitz  # PyMuPDF
from PIL import Image
import io
import os

pdf_path = "data.pdf"
output_dir = "images_webp"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)

for page_index in range(len(doc)):
    page = doc.load_page(page_index)
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        # Pillow로 이미지 열기
        img_pil = Image.open(io.BytesIO(image_bytes))
        # WebP로 저장 (최고 화질 옵션)
        webp_filename = f"{output_dir}/page_{page_index+1}_image_{img_index}.webp"
        img_pil.save(webp_filename, "WEBP", quality=100, method=6)
        print(f"Saved image: {webp_filename}")
