import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

global_path = BASE_DIR / "dataset" / "cropped" / "01_signature_global.jpg"
otsu_path = BASE_DIR / "dataset" / "cropped" / "01_signature_otsu.jpg"

# Baca hasil threshold
global_img = cv2.imread(str(global_path), cv2.IMREAD_GRAYSCALE)
otsu_img = cv2.imread(str(otsu_path), cv2.IMREAD_GRAYSCALE)

# Hitung jumlah piksel foreground (piksel putih)
global_area = cv2.countNonZero(global_img)
otsu_area = cv2.countNonZero(otsu_img)

# Hitung total piksel
total_pixels = global_img.shape[0] * global_img.shape[1]

# Hitung persentase foreground
global_percentage = (global_area / total_pixels) * 100
otsu_percentage = (otsu_area / total_pixels) * 100

print("GLOBAL THRESHOLD")
print("Foreground:", global_area)
print("Persentase:", round(global_percentage, 2), "%")

print("\nOTSU THRESHOLD")
print("Foreground:", otsu_area)
print("Persentase:", round(otsu_percentage, 2), "%")