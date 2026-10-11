import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "dataset" / "cropped" / "01_signature_gray.jpg"

global_path = BASE_DIR / "dataset" / "cropped" / "01_signature_global_inv.jpg"
otsu_path = BASE_DIR / "dataset" / "cropped" / "01_signature_otsu_inv.jpg"

# Baca citra grayscale
gray = cv2.imread(str(input_path), cv2.IMREAD_GRAYSCALE)

# Global Threshold Inverse
_, global_threshold = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY_INV
)

# Otsu Threshold Inverse
_, otsu_threshold = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# Simpan hasil
cv2.imwrite(str(global_path), global_threshold)
cv2.imwrite(str(otsu_path), otsu_threshold)