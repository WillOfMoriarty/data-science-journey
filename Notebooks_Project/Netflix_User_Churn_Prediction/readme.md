# 📌 Project Overview
Project ini bertujuan untuk memprediksi Churn Status pengguna layanan streaming berdasarkan data profil pelanggan dan kebiasaan menonton. Meskipun data memiliki distribusi kelas yang cukup seimbang, model menghadapi tantangan signifikan dalam menemukan pola prediktif yang kuat.

# 📊 Dataset Metadata
Total Data: 1.000 baris
Target: Churn Status (Yes/No) (54% Churn, 46% Not Churn)
Features: 15 Fitur (Kombinasi Numerik & Kategorikal)

# 🔍 Exploratory Data Analysis (EDA) & Statistical Findings
  1. Hubungan Fitur Numerik (Korelasi Pearson)
Berdasarkan analisis korelasi, hampir seluruh fitur numerik menunjukkan nilai korelasi yang sangat rendah terhadap target (< 0.06). Ini mengindikasikan tidak adanya hubungan linear yang kuat.

<img width="751" height="682" alt="image" src="https://github.com/user-attachments/assets/a079f2e2-b450-4b6c-ba66-ee0cd93651d0" />

  2. Hubungan Fitur Kategorikal (Uji Chi-Square)
Dilakukan uji Chi-Square untuk melihat keterkaitan fitur kategorikal terhadap Churn.
Hasil: Semua fitur (Region, Device, Plan, dll) memiliki P-Value > 0.05.
Kesimpulan: Secara statistik, fitur kategorikal yang tersedia tidak berpengaruh signifikan terhadap keputusan pengguna untuk churn.

<img width="984" height="483" alt="image" src="https://github.com/user-attachments/assets/04d07014-9c2e-48b1-a507-59f0a85b18ad" />
<img width="984" height="483" alt="image" src="https://github.com/user-attachments/assets/6bfba5ba-1a4f-4889-b63c-83dfeb6ae173" />
<img width="984" height="483" alt="image" src="https://github.com/user-attachments/assets/73a31aff-e0cd-4b67-98e7-a7fd9cd61ec1" />


# 🤖 Model Performance

Kami menguji tiga algoritma berbeda untuk melihat apakah model non-linear bisa menangkap pola tersembunyi.

| Model | Accuracy | ROC AUC |
| :--- | :---: | :---: |
| **Logistic Regression** | 0.52 | 0.50 |
| **Random Forest** | 0.54 | 0.51 |
| **XGBoost** | 0.54 | 0.54 |

<img width="982" height="583" alt="image" src="https://github.com/user-attachments/assets/adba97a5-97d6-4c3d-bcaf-2471f8c7fdcf" />
  
# 💡 Root Cause Analysis: Kenapa ROC AUC hanya ~0.5?
Skor AUC 0.5 setara dengan tebakan acak. Berdasarkan eksperimen ini, rendahnya performa model disebabkan oleh:
Data Noise: Fitur yang tersedia (seperti Age atau Income) terdistribusi secara acak di kedua kelas (Churn & Stay).
Missing Predictive Signals: Data tidak mencakup variabel perilaku kritis, seperti "Tren penurunan durasi tonton" atau "Riwayat interaksi CS dalam 7 hari terakhir".
Weak Correlation: Baik uji Pearson maupun Chi-Square mengonfirmasi bahwa tidak ada fitur yang memiliki "daya beda" (discriminatory power) yang cukup.

# 🚀 Key Takeaways (Lesson Learned)
Model vs Data: Model sekelas XGBoost sekalipun tidak bisa memberikan hasil maksimal jika data yang dimasukkan bersifat noise (prinsip Garbage In, Garbage Out).
Feature Engineering is King: Dalam masalah churn, fitur statis (profil) seringkali kalah penting dibandingkan fitur dinamis (perubahan perilaku).
Statistical Validation: Melakukan uji statistik di awal sangat membantu untuk memahami potensi performa model sebelum masuk ke tahap tuning.
