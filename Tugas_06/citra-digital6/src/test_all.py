import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_dir = BASE_DIR / "dataset" / "cropped"
output_dir = BASE_DIR / "results"

output_dir.mkdir(exist_ok=True)

# Kernel untuk morphology
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Batas awal area foreground
threshold_area = 2.0

image_files = [
    input_dir / "01_HighQuality_Enhanced_signature_crop.jpg",
    input_dir / "02_LowContrast_signature_crop.jpg",
    input_dir / "03_Blurred_signature_crop.jpg",
    input_dir / "04_HighNoise_signature_crop.jpg",
    input_dir / "05_LowResolution_Upsampled_signature_crop.jpg",
    input_dir / "06_Faded_Underexposed_signature_crop.jpg",
    input_dir / "07_ColorShift_WarmTint_signature_crop.jpg",
    input_dir / "08_JPEGCompression_Artifacts_signature_crop.jpg",
    input_dir / "09_CombinedDegradation_signature_crop.jpg",
]

for input_path in image_files:

    # Baca citra hasil crop
    image = cv2.imread(str(input_path))

    # Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Otsu Threshold Inverse
    _, binary = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # Morphological Opening
    opening = cv2.morphologyEx(
        binary,
        cv2.MORPH_OPEN,
        kernel
    )

    # Morphological Closing
    closing = cv2.morphologyEx(
        opening,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Hitung foreground
    foreground_pixels = cv2.countNonZero(closing)

    # Hitung total piksel
    total_pixels = closing.shape[0] * closing.shape[1]

    # Persentase foreground
    foreground_percentage = (
        foreground_pixels / total_pixels
    ) * 100

    # Aturan deteksi
    if foreground_percentage >= threshold_area:
        result = "SIGNATURE PRESENT"
    else:
        result = "SIGNATURE ABSENT"

    # Simpan hasil akhir
    output_path = (
        output_dir /
        f"{input_path.stem}_result.jpg"
    )

    cv2.imwrite(str(output_path), closing)

    print(input_path.name)
    print("Foreground:", foreground_pixels)
    print("Percentage:", round(foreground_percentage, 2), "%")
    print("Result:", result)
    print("-" * 40)