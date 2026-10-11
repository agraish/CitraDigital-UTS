import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "dataset" / "cropped" / "01_signature_otsu_inv.jpg"

opening_path = BASE_DIR / "dataset" / "cropped" / "01_signature_opening.jpg"
closing_path = BASE_DIR / "dataset" / "cropped" / "01_signature_closing.jpg"

# Baca hasil Otsu inverse
image = cv2.imread(str(input_path), cv2.IMREAD_GRAYSCALE)

# Kernel morfologi
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Morphological Opening
opening = cv2.morphologyEx(
    image,
    cv2.MORPH_OPEN,
    kernel
)

# Morphological Closing
closing = cv2.morphologyEx(
    opening,
    cv2.MORPH_CLOSE,
    kernel
)

# Simpan hasil
cv2.imwrite(str(opening_path), opening)
cv2.imwrite(str(closing_path), closing)