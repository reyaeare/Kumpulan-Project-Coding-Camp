# Submission-Machine-Learning
# Machine Learning Project: Clustering & Classification

## Deskripsi Project

Project ini merupakan submission akhir kelas Machine Learning yang menggabungkan pendekatan **unsupervised learning** dan **supervised learning** dalam satu alur proyek.

Pada tahap awal, dilakukan proses clustering untuk menghasilkan label atau kelas baru dari dataset tanpa label menggunakan metode unsupervised learning. Setelah label diperoleh, data tersebut digunakan untuk membangun model klasifikasi yang mampu memprediksi kelas berdasarkan fitur yang tersedia.

Dataset yang digunakan berasal dari modifikasi dataset **Bank Transaction Dataset for Fraud Detection**.

---

# Tujuan Project

Project ini bertujuan untuk:

* Melakukan segmentasi data menggunakan teknik clustering
* Menghasilkan label baru dari data tanpa label
* Mengembangkan model klasifikasi berdasarkan hasil clustering
* Membandingkan performa beberapa model machine learning
* Mengimplementasikan workflow machine learning end-to-end

---

# Dataset

Dataset yang digunakan:

* `data_clustering.csv`
* `data_clustering_inverse.csv`

Dataset ini merupakan hasil modifikasi dari dataset transaksi perbankan untuk kebutuhan pembelajaran clustering dan classification.

---

# Tahapan Project

## 1. Data Understanding

Pada tahap ini dilakukan:

* Eksplorasi dataset
* Identifikasi tipe data
* Analisis distribusi data
* Pemeriksaan missing value dan outlier

---

## 2. Data Preprocessing

Tahap preprocessing meliputi:

* Data cleaning
* Feature scaling
* Encoding data kategorikal
* Feature selection
* PCA (Principal Component Analysis)

---

## 3. Clustering (Unsupervised Learning)

Metode clustering digunakan untuk menghasilkan label atau kelompok data.

Algoritma yang digunakan:

* K-Means Clustering

Evaluasi clustering dilakukan menggunakan:

* Elbow Method
* Silhouette Score

Output clustering:

* `model_clustering.h5`
* `PCA_model_clustering.h5`

---

## 4. Classification (Supervised Learning)

Label hasil clustering digunakan sebagai target klasifikasi.

Model yang digunakan:

* Decision Tree
* Random Forest

File model:

* `decision_tree_model.h5`
* `explore_random_forest_classification.h5`
* `tuning_classification.h5`

Evaluasi model dilakukan menggunakan:

* Accuracy
* Precision
* Recall
* F1-Score

---

# Struktur Repository

```bash id="k1h34o"
Machine-Learning-Project/
│
├── README.md
├── data_clustering.csv
├── data_clustering_inverse.csv
├── model_clustering.h5
├── PCA_model_clustering.h5
├── decision_tree_model.h5
├── explore_random_forest_classification.h5
├── tuning_classification.h5
├── [Clustering]_Submission_Akhir_BMLP.ipynb
└── [Klasifikasi]_Submission_Akhir_BMLP.ipynb
```

---

# Teknologi yang Digunakan

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Joblib

---

# Hasil Project

## Clustering

Model clustering berhasil membentuk beberapa cluster berdasarkan karakteristik transaksi data.

## Classification

Model klasifikasi mampu memprediksi label hasil clustering dengan performa evaluasi yang baik.

---

# Cara Menjalankan Project

## 1. Clone Repository

```bash id="v97v0l"
git clone https://github.com/username/repository-name.git
```

---

## 2. Install Dependencies

```bash id="v6a9s5"
pip install -r requirements.txt
```

---

## 3. Jalankan Notebook

Buka notebook menggunakan Jupyter Notebook atau Google Colab:

* `[Clustering]_Submission_Akhir_BMLP.ipynb`
* `[Klasifikasi]_Submission_Akhir_BMLP.ipynb`

---

# Author

**Seni Yanti**
Mahasiswa Statistika Universitas Halu Oleo
Data Scientist Cohort at DBS Foundation
