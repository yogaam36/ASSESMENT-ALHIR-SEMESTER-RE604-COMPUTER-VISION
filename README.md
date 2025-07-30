# ASSESMENT-AkHIR-SEMESTER-RE604-COMPUTER-VISION
# Optical Character Recognition (OCR) pada plat nomor kendaraan menggunakan Visual Language Model (VLM)

# Deskripsi
Proyek ini bertujuan untuk mengembangkan sistem Optical Character Recognition (OCR) yang mampu mengenali dan mengekstrak teks dari plat nomor kendaraan secara otomatis. Sistem ini memanfaatkan Visual Language Model (VLM) — yaitu model kecerdasan buatan multimodal yang mampu memahami gambar dan teks secara bersamaan, seperti LLaVA atau BakLLaVA

# Langkah Pengerjaan

# 1. Siapkan Dataset
Dataset harus berupa:
* Folder berisi gambar plat nomor
* File .csv berisi ground truth

# 2. Jalankan LMStudio
Load model LLaVA, BakLLaVA, atau model multimodal lain
Pastikan model dapat menerima gambar + prompt, dan aktif di server lokal, misalnya http://localhost:11434

# 3. Prompt OCR
Gunakan prompt standar berikut:
What is the license plate number shown in this image? Respond only with the plate number.

# 4. Python Script (pengiriman gambar, evaluasi CER)
Jalankan program python

# 5. Evaluasi Hasil Prediksi
setelah dapat hasil_prediksi.csv jalankan program Evaluasi_Hasil_prediksi nanti akan ketemu hasil dari prediksi yang gagal dan sukses
