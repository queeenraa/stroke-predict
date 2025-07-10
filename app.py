import streamlit as st
import numpy as np
import pickle

# Load model dan scaler
model = pickle.load(open('stroke_best_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Judul
st.title("🧠 Prediksi Risiko Stroke")
st.caption("📋 Masukkan data pasien untuk memprediksi kemungkinan risiko stroke.")
st.markdown("---")

# Input pengguna dengan pilihan kosong di awal
gender = st.selectbox("🧑 Jenis Kelamin", ['-- Pilih --', 'Laki-laki', 'Perempuan'])
age = st.slider("🎂 Umur (Tahun)", min_value=1, max_value=100, value=30)
hypertension = st.selectbox("💓 Apakah memiliki hipertensi?", ['-- Pilih --', 'Tidak', 'Ya'])
heart_disease = st.selectbox("❤️ Apakah memiliki penyakit jantung?", ['-- Pilih --', 'Tidak', 'Ya'])
ever_married = st.selectbox("💍 Status Pernikahan", ['-- Pilih --', 'Belum Menikah', 'Sudah Menikah'])
work_type = st.selectbox("💼 Jenis Pekerjaan", ['-- Pilih --', 'Anak-anak', 'Pegawai Negeri', 'Belum Pernah Bekerja', 'Swasta', 'Wiraswasta'])
residence_type = st.selectbox("🏡 Tempat Tinggal", ['-- Pilih --', 'Perkotaan', 'Pedesaan'])
avg_glucose = st.number_input("🩸 Rata-rata Glukosa Darah (mg/dL)", min_value=0.0, step=0.1,
                              help="Normal: 70–140 mg/dL. Di atas 140 tergolong tinggi.")
bmi = st.number_input("📏 Nilai BMI (Body Mass Index)", min_value=0.0, step=0.1)

# Hitung BMI otomatis
with st.expander("💡 Hitung BMI Otomatis (Opsional)"):
    col1, col2 = st.columns(2)
    with col1:
        berat = st.number_input("⚖️ Berat Badan (kg)", min_value=0.0, step=0.1)
    with col2:
        tinggi = st.number_input("📏 Tinggi Badan (cm)", min_value=0.0, step=0.1)

    if berat > 0 and tinggi > 0:
        hitung_bmi = round(berat / ((tinggi / 100) ** 2), 2)
        st.info(f"📏 BMI yang dihitung: **{hitung_bmi}**")
        bmi = hitung_bmi  # override nilai BMI manual jika diisi

smoking_status = st.selectbox("🚬 Status Merokok", ['-- Pilih --', 'Tidak Pernah Merokok', 'Pernah Merokok', 'Masih Merokok', 'Tidak Diketahui'])

# Validasi semua input wajib terisi
form_valid = all([
    gender != '-- Pilih --',
    hypertension != '-- Pilih --',
    heart_disease != '-- Pilih --',
    ever_married != '-- Pilih --',
    work_type != '-- Pilih --',
    residence_type != '-- Pilih --',
    smoking_status != '-- Pilih --',
    age > 0,
    avg_glucose > 0,
    bmi > 0
])

# Prediksi hanya jika input valid
if st.button("🚀 Prediksi Risiko Stroke"):
    if not form_valid:
        st.warning("⚠️ Harap lengkapi semua input terlebih dahulu.")
    else:
        input_data = np.array([[  
            0 if gender == 'Laki-laki' else 1,
            age,
            1 if hypertension == 'Ya' else 0,
            1 if heart_disease == 'Ya' else 0,
            1 if ever_married == 'Sudah Menikah' else 0,
            ['Anak-anak', 'Pegawai Negeri', 'Belum Pernah Bekerja', 'Swasta', 'Wiraswasta'].index(work_type),
            0 if residence_type == 'Perkotaan' else 1,
            avg_glucose,
            bmi,
            ['Pernah Merokok', 'Tidak Pernah Merokok', 'Masih Merokok', 'Tidak Diketahui'].index(smoking_status)
        ]])

        # Normalisasi input
        scaled_input = scaler.transform(input_data)

        # Prediksi
        prediction = model.predict(scaled_input)[0]
        if prediction == 1:
            st.error("⚠️ Berdasarkan data yang diberikan, pasien **berisiko terkena stroke**.")
        else:
            st.success("✅ Berdasarkan data yang diberikan, pasien **tidak berisiko stroke**.")

# Footer
st.markdown("---")
st.markdown("© 2025 Farhan & Laura — All rights reserved 💖")
