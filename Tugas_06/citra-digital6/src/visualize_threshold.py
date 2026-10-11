import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_dir = BASE_DIR / "dataset" / "cropped"
output_dir = BASE_DIR / "results" / "threshold_visual"

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

    comparison = cv2.hconcat([
        global_threshold,
        otsu_threshold
    ])

    output_path = (
        output_dir /
        f"{input_path.stem}_comparison.jpg"
    )

    cv2.imwrite(
        str(output_path),
        comparison
    )