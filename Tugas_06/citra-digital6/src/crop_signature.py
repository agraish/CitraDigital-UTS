from PIL import Image, ImageOps
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_dir = BASE_DIR / "dataset" / "raw"
output_dir = BASE_DIR / "dataset" / "cropped"

output_dir.mkdir(exist_ok=True)

# Koordinat crop yang sudah diuji pada gambar 01
left = 300
top = 1600
right = 1500
bottom = 2350

image_files = sorted(input_dir.glob("*.jpg"))

for input_path in image_files:

    image = Image.open(input_path)

    # Terapkan orientasi EXIF
    image = ImageOps.exif_transpose(image)

    # Crop area tanda tangan Rektor
    cropped = image.crop((left, top, right, bottom))

    output_path = output_dir / f"{input_path.stem}_signature_crop.jpg"

    cropped.save(output_path)