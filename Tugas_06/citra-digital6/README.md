# Deteksi Tanda Tangan Rektor pada Dokumen Ijazah

## Deskripsi

Proyek ini merupakan implementasi pengolahan citra digital untuk mendeteksi keberadaan tanda tangan Rektor pada area tertentu dari dokumen ijazah.

Tahapan pengolahan citra yang digunakan meliputi:

1. Crop area tanda tangan Rektor.
2. Konversi citra menjadi grayscale.
3. Global Threshold.
4. Otsu Threshold.
5. Perbandingan hasil thresholding.
6. Operasi morfologi opening dan closing.
7. Perhitungan jumlah piksel foreground.
8. Penentuan keberadaan tanda tangan berdasarkan persentase foreground.

## Dataset

Dataset terdiri dari 9 citra dokumen dengan kondisi kualitas yang berbeda:

- High Quality Enhanced
- Low Contrast
- Blurred
- High Noise
- Low Resolution Upsampled
- Faded Underexposed
- Color Shift Warm Tint
- JPEG Compression Artifacts
- Combined Degradation

Kesembilan citra tersebut digunakan sebagai data yang mengandung tanda tangan Rektor.

## Metode Pengolahan

### Grayscale

Citra berwarna dikonversi menjadi grayscale untuk menyederhanakan informasi intensitas sebelum proses segmentasi.

### Global Threshold

Global Threshold menggunakan nilai ambang tetap sebesar 127 untuk memisahkan foreground dan background.

### Otsu Threshold

Otsu Threshold menentukan nilai ambang secara otomatis berdasarkan distribusi intensitas piksel.

### Morfologi

Operasi opening digunakan untuk mengurangi noise kecil, sedangkan closing digunakan untuk membantu menghubungkan bagian foreground yang terputus.

Kernel morfologi yang digunakan berukuran 3 x 3.

### Deteksi Tanda Tangan

Persentase foreground dihitung menggunakan jumlah piksel foreground dibandingkan dengan jumlah seluruh piksel pada area crop.

Pada pengujian data positif, batas awal yang digunakan adalah 2%.

Jika:

Foreground percentage >= 2%

maka hasil:

SIGNATURE PRESENT

Jika kurang dari 2%, maka:

SIGNATURE ABSENT

Nilai 2% merupakan parameter eksperimen pada dataset yang digunakan dan belum divalidasi menggunakan dataset negatif yang memadai.

## Struktur Folder

citra-digital6/
|
|-- dataset/
|   |-- absent/
|   |-- cropped/
|   |-- present/
|   `-- raw/
|
|-- results/
|   |-- final/
|   |-- histogram/
|   |-- morphology/
|   |-- threshold_comparison/
|   `-- threshold_visual/
|
|-- src/
|   |-- compare_threshold.py
|   |-- create_absent.py
|   |-- crop_signature.py
|   |-- detect_signature.py
|   |-- grayscale.py
|   |-- histogram.py
|   |-- hitung_area.py
|   |-- main.py
|   |-- morphology.py
|   |-- morphology_all.py
|   |-- test_all.py
|   |-- threshold.py
|   `-- visualize_threshold.py
|
|-- README.md
`-- requirements.txt

## Instalasi

Pastikan Python sudah terpasang.

Install library yang diperlukan dengan:

pip install -r requirements.txt

## Menjalankan Program Utama

Jalankan:

python src/main.py

Program akan memproses 9 citra crop dan menghasilkan informasi jumlah foreground, persentase foreground, serta hasil deteksi.

## Pengujian Threshold

Untuk membandingkan Global Threshold dan Otsu Threshold:

python src/compare_threshold.py

## Histogram

Untuk menghasilkan histogram grayscale:

python src/histogram.py

## Operasi Morfologi

Untuk menjalankan opening dan closing pada seluruh citra:

python src/morphology_all.py

## Visualisasi Threshold

Untuk menghasilkan perbandingan visual Global Threshold dan Otsu:

python src/visualize_threshold.py

## Hasil Pengujian

Pada pengujian terhadap 9 citra yang mengandung tanda tangan Rektor, seluruh citra menghasilkan:

SIGNATURE PRESENT

Persentase foreground setelah proses Otsu dan morfologi berada pada rentang:

2.83% - 5.05%

Hasil perbandingan threshold menunjukkan bahwa pada beberapa citra dengan kualitas rendah, terutama citra Low Contrast dan Blurred, Global Threshold menghasilkan area foreground yang jauh lebih kecil dibandingkan Otsu.

Contohnya:

Low Contrast
Global : 0.40%
Otsu   : 3.18%

Blurred
Global : 0.70%
Otsu   : 5.04%

Hal tersebut menunjukkan bahwa Otsu lebih mampu mempertahankan area foreground pada kondisi citra tersebut.

Namun, hasil ini tidak berarti Otsu selalu lebih baik untuk semua kondisi citra. Kesimpulan tersebut terbatas pada hasil eksperimen dataset yang digunakan.

## Catatan

Target deteksi pada proyek ini adalah tanda tangan Rektor. Tanda tangan lain pada dokumen, seperti tanda tangan Dekan, tidak digunakan sebagai target.

Dataset negatif yang valid masih diperlukan untuk menguji kemampuan sistem dalam membedakan kondisi SIGNATURE PRESENT dan SIGNATURE ABSENT secara lengkap.