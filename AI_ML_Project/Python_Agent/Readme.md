📌 Project Description

Project ini merupakan AI-powered Data Analyst Chatbot yang memungkinkan user untuk:

Bertanya tentang data penjualan
Melakukan analisis data otomatis
Melakukan query database menggunakan bahasa natural

Aplikasi dibangun menggunakan Streamlit sebagai UI dan LLM Gemini sebagai reasoning engine, dengan pendekatan Agent-based system (bukan Traditional RAG).

🎯 Objectives
Membangun chatbot data analyst berbasis AI
Mengimplementasikan SQL Agent untuk database analysis
Mengimplementasikan Python Agent untuk analisis data berbasis pandas
Menyediakan UI interaktif untuk eksplorasi data

📊 Dataset

Dataset berisi data penjualan dengan kolom utama:
Order_Date
Product
Category
Quantity
Price
Total_Sales
Region

Dataset digunakan dalam dua bentuk:
CSV → untuk Python Agent (pandas analysis)
SQLite DB → untuk SQL Agent (database querying)

🤖 System Architecture
1️⃣ SQL Agent

Digunakan untuk:

Query database menggunakan natural language
Otomatis generate SQL query
Eksekusi ke SQLite database
Tools yang digunakan:
LangChain SQL Agent
SQLite
Gemini LLM

Contoh kemampuan:
Menampilkan tabel
Agregasi data (SUM, COUNT, GROUP BY)
Filter data berdasarkan kondisi

2️⃣ Python Agent (Data Analysis Agent)

Digunakan untuk:
Analisis data berbasis pandas
Perhitungan statistik
Filtering dan agregasi data
Menampilkan hasil dalam bentuk tabel

Keamanan:
Tidak mengizinkan import
Tidak mengizinkan file system access
Hanya menjalankan pandas operation pada dataframe df

3️⃣ Streamlit Chatbot UI

Fitur utama:
Input pertanyaan user
Eksekusi analisis data secara otomatis
Menampilkan hasil dalam bentuk tabel atau text
Interaktif dan mudah digunakan

🚀 Conclusion

Project ini menunjukkan implementasi AI Agent untuk:
Analisis data
Query database
Natural language interaction
Pendekatan agent-based membuat sistem lebih fleksibel, aman, dan powerful dibandingkan chatbot berbasis retrieval biasa.