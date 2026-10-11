from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "dataset" / "cropped" / "01_signature_crop.jpg"
output_path = BASE_DIR / "dataset" / "cropped" / "01_signature_gray.jpg"

# Baca hasil crop
image = Image.open(input_path)

# Ubah ke grayscale
gray = image.convert("L")

# Simpan hasil grayscale
gray.save(output_path)