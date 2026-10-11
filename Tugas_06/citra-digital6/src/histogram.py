import cv2
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_dir = BASE_DIR / "dataset" / "cropped"
output_dir = BASE_DIR / "results" / "histogram"

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

    histogram = cv2.calcHist(
        [gray],
        [0],
        None,
        [256],
        [0, 256]
    )

    plt.figure(figsize=(8, 4))
    plt.plot(histogram)
    plt.xlim([0, 256])
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")
    plt.title(f"Histogram - {input_path.stem}")
    plt.tight_layout()

    output_path = (
        output_dir /
        f"{input_path.stem}_histogram.png"
    )

    plt.savefig(output_path)
    plt.close()