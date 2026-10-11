import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_dir = BASE_DIR / "dataset" / "cropped"
output_dir = BASE_DIR / "results" / "threshold_comparison"

output_dir.mkdir(parents=True, exist_ok=True)

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

    gray = cv2.imread(
        str(input_path),
        cv2.IMREAD_GRAYSCALE
    )

    _, global_threshold = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY_INV
    )

    _, otsu_threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    global_area = cv2.countNonZero(global_threshold)
    otsu_area = cv2.countNonZero(otsu_threshold)

    total_pixels = gray.shape[0] * gray.shape[1]

    global_percentage = (
        global_area / total_pixels
    ) * 100

    otsu_percentage = (
        otsu_area / total_pixels
    ) * 100

    global_output = (
        output_dir /
        f"{input_path.stem}_global.jpg"
    )

    otsu_output = (
        output_dir /
        f"{input_path.stem}_otsu.jpg"
    )

    cv2.imwrite(
        str(global_output),
        global_threshold
    )

    cv2.imwrite(
        str(otsu_output),
        otsu_threshold
    )

    print(input_path.name)
    print(
        "Global:",
        round(global_percentage, 2),
        "%"
    )
    print(
        "Otsu:",
        round(otsu_percentage, 2),
        "%"
    )
    print("-" * 40)