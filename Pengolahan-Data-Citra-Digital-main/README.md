# Data Citra Digital & Computer Vision

Notebook eksplorasi fitur statistik & tekstur pada citra digital menggunakan Python. Berisi ilustrasi bagaimana **histogram** dan **Gray-Level Co-occurrence Matrix (GLCM)** dapat digunakan untuk mengekstraksi karakteristik citra (tekstur, kecerahan, kontras) yang umum dipakai sebagai fitur pada tugas *computer vision* dan *image classification*.

## 📂 Isi Notebook

| No | Bagian | Deskripsi |
|---|---|---|
| 1 | **Histogram — Low vs High Texture** | Membandingkan citra dengan tekstur halus (*low texture*) dan citra bertekstur kasar (*high texture*) menggunakan local standard deviation (sliding window 7×7) |
| 2 | **Histogram — Skewness** | Membuat citra sintetis dengan distribusi piksel *positive skew* dan *negative skew* (distribusi Beta), lalu menghitung nilai skewness histogram-nya |
| 3 | **Histogram — Kurtosis** | Membandingkan citra dengan kurtosis tinggi (didominasi nilai konstan + sedikit titik ekstrem) dan kurtosis rendah (distribusi uniform) |
| 4 | **GLCM (Gray-Level Co-occurrence Matrix)** | Menghitung matriks co-occurrence dan mengekstraksi fitur Haralick (*contrast, homogeneity, energy, correlation, dissimilarity*) dari citra contoh 4×4 dan 8×8 |

## 🧠 Konsep yang Dibahas

- **Local Standard Deviation** — mengukur variasi intensitas piksel secara lokal untuk mendeteksi tingkat tekstur suatu area citra.
- **Skewness** — mengukur kemencengan distribusi intensitas piksel (citra gelap vs citra terang dominan).
- **Kurtosis** — mengukur "keruncingan" distribusi intensitas piksel (banyak nilai ekstrem vs distribusi merata).
- **GLCM & Haralick Features** — teknik ekstraksi fitur tekstur berbasis hubungan spasial antar-piksel bertetangga, sering dipakai sebagai fitur tambahan (feature engineering) pada model klasifikasi citra klasik maupun sebagai pelengkap deep learning.

## 🛠️ Teknologi & Library

- Python 3
- [NumPy](https://numpy.org/) — operasi array & pembuatan citra sintetis
- [Matplotlib](https://matplotlib.org/) — visualisasi citra dan histogram
- [SciPy](https://scipy.org/) (`scipy.stats`) — perhitungan skewness & kurtosis
- [scikit-image](https://scikit-image.org/) (`skimage.feature`) — perhitungan GLCM dan Haralick features
- Pandas — (opsional) untuk menyajikan hasil fitur dalam bentuk tabel

## 🚀 Cara Menjalankan

1. Clone repository ini:
   ```bash
   git clone <url-repo-kamu>
   cd <nama-repo>
   ```
2. Install dependency yang dibutuhkan:
   ```bash
   pip install numpy matplotlib scipy scikit-image pandas
   ```
3. Buka notebook dengan Jupyter Notebook/JupyterLab, atau upload ke Google Colab / Kaggle:
   ```bash
   jupyter notebook Data_Citra_Digital_Computer_Vision.ipynb
   ```
4. Jalankan seluruh cell secara berurutan (`Run All`).

> Semua citra pada notebook ini bersifat **sintetis** (dibuat menggunakan NumPy, bukan file gambar eksternal), sehingga notebook bisa langsung dijalankan tanpa perlu menyiapkan dataset.

## 📊 Output yang Dihasilkan

- Visualisasi peta lokal standar deviasi (local texture map) beserta histogramnya
- Perbandingan citra dan histogram untuk berbagai nilai skewness & kurtosis
- Nilai fitur Haralick (contrast, homogeneity, energy, correlation, dissimilarity) dari GLCM, ditampilkan dalam bentuk print/table

## 📚 Referensi

- Haralick, R.M., Shanmugam, K., & Dinstein, I. (1973). *Textural Features for Image Classification*. IEEE Transactions on Systems, Man, and Cybernetics.
- [Dokumentasi scikit-image — `graycomatrix` & `graycoprops`](https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.graycomatrix)
- [Dokumentasi SciPy Stats — skew & kurtosis](https://docs.scipy.org/doc/scipy/reference/stats.html)

## ✍️ Catatan

Notebook ini dibuat untuk keperluan pembelajaran/eksplorasi konsep dasar ekstraksi fitur tekstur pada citra digital, sebagai bagian dari pembelajaran **Computer Vision** dan dapat dijadikan referensi untuk tahap *feature engineering* pada proyek klasifikasi citra.
