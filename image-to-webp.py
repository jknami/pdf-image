import os
from PIL import Image

# 변환할 이미지가 들어있는 폴더 경로
input_folder = r"D:\jknam_FTP\분양현장별\여의대방_더마크원\이미지_실사"
# 변환된 webp 파일을 저장할 폴더 경로
output_folder = r"D:\jknam_FTP\분양현장별\여의대방_더마크원\이미지_실사\webp"
os.makedirs(output_folder, exist_ok=True)

# 변환할 이미지 확장자 목록
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')

for filename in os.listdir(input_folder):
    if filename.lower().endswith(image_extensions):
        input_path = os.path.join(input_folder, filename)
        output_name = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(output_folder, output_name)
        try:
            with Image.open(input_path) as img:
                img.save(output_path, "WEBP", quality=100, method=6)
            print(f"변환 완료: {output_path}")
        except Exception as e:
            print(f"변환 실패: {input_path}, 오류: {e}")
