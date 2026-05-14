import pyodbc
import pandas as pd

df = pd.read_csv("data/cleaned/games_steam_cleaned.csv")

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-3753H5N\\SQLEXPRESS;"
    "Database=SteamMarketDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO steam_games (title, price_clean, review_clean, discount_clean)
        VALUES (?, ?, ?, ?)
    """,
    row['title'],
    row['price_clean'],
    row['review_clean'],
    row['discount_clean'])

conn.commit()
cursor.close()
conn.close()