import pandas as pd

df = pd.read_csv("data/cleaned/steam_games_data_cleaned.csv")

def clean_review(review):
    review = review.split("<br>")[0]
    return review

df["review_clean"] = df["review"].apply(clean_review)

def clean_discount(discount) :
    discount = discount.replace("%", "")
    discount = discount.replace("-", "")
    return int(discount)

df["discount_clean"] = df["discount"].apply(clean_discount)

print(df.head())
print(df.info())

df.to_csv("data/cleaned/games_steam_cleaned.csv", index=False)