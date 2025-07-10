# 🧠 Prediksi Risiko Stroke dengan Random Forest dan Streamlit

Proyek ini bertujuan untuk memprediksi risiko stroke pada pasien menggunakan algoritma machine learning Random Forest dan menampilkannya dalam antarmuka web interaktif berbasis Streamlit.

---

## 📊 Deskripsi Proyek

Stroke adalah salah satu penyebab utama kematian secara global. Dengan pendekatan machine learning, proyek ini membangun model prediktif berbasis dataset medis dari Kaggle untuk mendeteksi kemungkinan risiko stroke berdasarkan fitur-fitur seperti:

- Jenis kelamin
- Umur
- Tekanan darah
- Penyakit jantung
- Status menikah
- Tipe pekerjaan
- Jenis tempat tinggal
- Rata-rata kadar glukosa darah
- Body Mass Index (BMI)
- Status merokok

---

## 🗂️ Dataset

- **Sumber:** Kaggle – [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

---

## 🔧 Tahapan Proyek

### 1. Prapemrosesan Data
- Mengisi nilai kosong pada kolom BMI dengan nilai median
- Encoding kolom kategorikal
- Deteksi dan penghapusan outlier

### 2. Eksplorasi Data (EDA)
- Analisis distribusi umur, BMI, dan variabel target
- Korelasi antar fitur

### 3. Penyeimbangan Data
- Menggunakan SMOTE (Synthetic Minority Over-sampling Technique)

### 4. Pemodelan dan Evaluasi
- Algoritma: `RandomForestClassifier(class_weight='balanced')`
- Tuning hyperparameter dengan `GridSearchCV`
- Evaluasi menggunakan recall, f1-score, dan confusion matrix

### 5. Deployment
- Aplikasi dibangun menggunakan **Streamlit**
- Input data interaktif + perhitungan otomatis BMI
- Prediksi ditampilkan secara real-time

---

## 📈 Hasil Evaluasi

- **Accuracy:** 94%
- **Recall (stroke):** 0.06
- **F1-score (stroke):** 0.07


---

## 🌐 Tautan Proyek

- 🔗 [Google Colab](https://colab.research.google.com/drive/1ANh48FG3C1CH3fYsgoUJmPmLI7oAXrDR?usp=sharing)
- 💻 [GitHub Repository](https://github.com/queeenraa/stroke-predict)
- 🌍 [Live Streamlit App](https://stroke-predict-my.streamlit.app)

---

## 👥 Anggota Kelompok

- Farhan Mutawakkil Haidar — 22416255201133  
- Laura Amelia — 22416255201146

---

## 📄 Lisensi

© 2025 Farhan & Laura — All rights reserved.
