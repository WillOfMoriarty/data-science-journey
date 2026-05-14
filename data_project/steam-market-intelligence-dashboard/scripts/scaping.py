import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent" : "Mozilla/5.0"
}

all_data = []
for page in range (1, 6) :
    print(f"Scraping Page {page}")
    url = "https://store.steampowered.com/search/?filter=topsellers&page={page}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    games = soup.find_all("a", class_="search_result_row")

    for game in games :
        title = game.find("span", class_="title")
        price = game.find("div", class_="discount_final_price")
        review = game.find("span", class_="search_review_summary")
        discount = game.find("div", class_="discount_pct")

        if title:
            title = title.text.strip()
        else :
            title = None
        
        if price :
            price = price.text.strip()
        else :
            price = "Free"

        review = review['data-tooltip-html'].strip() if review and review.has_attr('data-tooltip-html') else "No Reviews"
        discount = discount.text.strip() if discount else "0%"

        all_data.append({
            'title' : title,
            'price' : price,
            'review' : review,
            'discount' : discount
        })

    time.sleep(2)

df = pd.DataFrame(all_data)
print(df.head(10))

print(f"\nTotal data: {len(df)}")

df.to_csv("data/raw/steam_games_data.csv", index=False)
