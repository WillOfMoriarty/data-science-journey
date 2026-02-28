
import streamlit as st
import pandas as pd
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI


# ===== CONFIG =====
st.set_page_config(page_title='AI Data Analyst', layout='wide')

# ===== LOAD DATA =====
def load_data():
  df = pd.read_csv('product_sales_dataset.csv')
  df["Order_Date"] = pd.to_datetime(df["Order_Date"])
  return df

df= load_data()

# ===== LOAD LLM =====
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# ===== SAFETY =====
def is_code_safe(code: str) -> bool:
    blocked_keywords = [
        "import", "open(", "exec(", "eval(", "__",
        "os.", "sys.", "subprocess", "shutil",
        "read_csv", "read_excel"
    ]
    if "/" in code:
        return False
    return not any(k in code for k in blocked_keywords)

def run_python_code_safe(code: str):
    if not is_code_safe(code):
        return "❌ Permintaan ditolak karena kebijakan keamanan."
    try:
        local_vars = {"df": df}
        exec(code, {}, local_vars)
        return local_vars.get("result", "⚠️ Tidak ada hasil.")
    except Exception as e:
        return f"❌ Error: {str(e)}"

def ask_agent_safe(question: str):
    prompt = f"""
    Kamu adalah data analyst.

    Data tersedia dalam dataframe bernama df.
    Kolom yang tersedia:
    {list(df.columns)}

    ATURAN:
    - Hanya gunakan pandas
    - Jangan gunakan import apapun
    - Simpan jawaban akhir ke variabel bernama result
    - Jika hasil berupa tabel, gunakan DataFrame

    Hanya tulis kode Python. Jangan beri penjelasan.

    Pertanyaan:
    {question}
    """
    response = llm.invoke(prompt)
    code = response.content.strip("```python").strip("```")
    return run_python_code_safe(code)

# ===== UI =====
st.title("🤖 AI Data Analyst Chatbot")

question = st.text_input("Tanya soal data penjualan:")

if st.button("Analisa"):
    with st.spinner("Menganalisa data..."):
        result = ask_agent_safe(question)

    if isinstance(result, pd.DataFrame):
        st.dataframe(result)
    else:
        st.write(result)
