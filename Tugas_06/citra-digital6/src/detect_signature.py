import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "dataset" / "cropped" / "01_signature_closing.jpg"

# Baca hasil morphology
image = cv2.imread(str(input_path), cv2.IMREAD_GRAYSCALE)

# Hitung jumlah piksel foreground
foreground_pixels = cv2.countNonZero(image)

# Hitung total piksel
total_pixels = image.shape[0] * image.shape[1]

# Hitung persentase foreground
foreground_percentage = (foreground_pixels / total_pixels) * 100

# Aturan sederhana
threshold_area = 2.0

if foreground_percentage >= threshold_area:
    result = "SIGNATURE PRESENT"
else:
    result = "SIGNATURE ABSENT"

print("Foreground pixels:", foreground_pixels)
print("Total pixels:", total_pixels)
print("Foreground percentage:", round(foreground_percentage, 2), "%")
print("Result:", result)