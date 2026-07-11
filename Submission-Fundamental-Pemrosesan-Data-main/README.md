# Submission-Fundamental-Pemrosesan-Data

## Deskripsi Project

Project ini merupakan submission akhir untuk kelas **Belajar Fundamental Pemrosesan Data**.
Pada project ini dibangun sebuah **ETL (Extract, Transform, Load) Pipeline** sederhana menggunakan Python untuk mengambil data produk fashion dari website kompetitor, membersihkan dan memproses data, lalu menyimpannya ke dalam format yang siap digunakan oleh tim data science.

Website sumber data:
https://fashion-studio.dicoding.dev

---

## Latar Belakang

Sebagai seorang data engineer di perusahaan retail fashion, tugas utama project ini adalah membantu perusahaan melakukan monitoring terhadap produk dan harga kompetitor.

Data yang diperoleh nantinya dapat digunakan untuk:

* Analisis harga kompetitor
* Monitoring produk fashion terbaru
* Pengambilan keputusan bisnis berbasis data
* Persiapan analisis lanjutan oleh tim data science

---

# ETL Pipeline

## 1. Extract

Pada tahap extract, sistem mengambil data produk dari website Fashion Studio menggunakan teknik web scraping.

Data yang diambil meliputi:

* Nama produk
* Harga produk
* Rating
* Warna
* Ukuran
* Gender
* Timestamp pengambilan data

---

## 2. Transform

Pada tahap transform dilakukan proses pembersihan dan persiapan data, seperti:

* Menghapus data duplikat
* Membersihkan format harga
* Mengubah tipe data
* Menangani missing value
* Standarisasi format data

---

## 3. Load

Data yang telah bersih kemudian disimpan ke dalam:

* File CSV (`products.csv`)
* Google Sheets (opsional)

---

# Struktur Project

```bash
Submission-Fundamental-Pemrosesan-Data/
│
├── tests/
├── utils/
├── main.py
├── products.csv
├── requirements.txt
├── submission.txt
└── README.md
```

---

# Teknologi yang Digunakan

* Python
* Pandas
* Requests
* BeautifulSoup4
* Google Sheets API
* Pytest

---

# Cara Menjalankan Project

## 1. Clone Repository

```bash
git clone https://github.com/username/repository-name.git
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Jalankan Program

```bash
python main.py
```

---

# Google Sheets API

File credential Google Sheets API (`google-sheets-api.json`) tidak disertakan dalam repository karena bersifat rahasia dan demi keamanan.

Jika ingin menjalankan fitur Google Sheets:

1. Buat Google Cloud Service Account
2. Download credential JSON
3. Rename file menjadi:

```bash
google-sheets-api.json
```

4. Simpan file pada root directory project

---

# Testing

Project ini menggunakan `pytest` untuk pengujian.

Menjalankan testing:

```bash
pytest
```

---

# Hasil Akhir

Pipeline berhasil:

* Mengekstrak data produk fashion dari website
* Membersihkan dan mentransformasi data
* Menyimpan data ke format yang siap digunakan

---

# Author

**Seni Yanti**
Mahasiswa Statistika Universitas Halu Oleo
Data Scientist Cohort at DBS Foundation
