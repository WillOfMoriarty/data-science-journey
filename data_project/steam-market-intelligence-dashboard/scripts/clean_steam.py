import pandas as pd

df = pd.read_csv("data/raw/steam_games_data.csv")

def clean_price(price) :
    if price == "Free":
        return 0

    # Delete Rp
    price = price.replace("Rp", "")
    # Delete Space
    price = price.replace(" ", "")

    return int(price)


df['price_clean'] = df['price'].apply(clean_price)
df = df.drop_duplicates()

print(df.head())
print(df.info())

df.to_csv("data/cleaned/steam_games_data_cleaned.csv", index=False)