import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_dir = BASE_DIR / "dataset" / "cropped"
output_dir = BASE_DIR / "results" / "morphology"

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

kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (3, 3)
)

for input_path in image_files:

    gray = cv2.imread(
        str(input_path),
        cv2.IMREAD_GRAYSCALE
    )

    _, binary = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    opening = cv2.morphologyEx(
        binary,
        cv2.MORPH_OPEN,
        kernel
    )

    closing = cv2.morphologyEx(
        opening,
        cv2.MORPH_CLOSE,
        kernel
    )

    foreground_pixels = cv2.countNonZero(closing)

    total_pixels = (
        closing.shape[0] *
        closing.shape[1]
    )

    foreground_percentage = (
        foreground_pixels /
        total_pixels
    ) * 100

    if foreground_percentage >= 2.0:
        result = "SIGNATURE PRESENT"
    else:
        result = "SIGNATURE ABSENT"

    output_path = (
        output_dir /
        f"{input_path.stem}_morphology.jpg"
    )

    cv2.imwrite(
        str(output_path),
        closing
    )

    print(input_path.name)
    print(
        "Foreground:",
        foreground_pixels
    )
    print(
        "Percentage:",
        round(foreground_percentage, 2),
        "%"
    )
    print("Result:", result)
    print("-" * 40)