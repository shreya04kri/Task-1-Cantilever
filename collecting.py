import os
import pandas as pd
from bs4 import BeautifulSoup

# Initialize the dictionary with lower-case keys
d = {'title': [], 'rating': [], 'price': [], 'link': []}

# Iterate through files in the 'data' directory
for file in os.listdir("data"):
    try:
        # Open and read the HTML file
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        # Extract the title
        t = soup.find('h2')
        title = t.get_text() if t else 'N/A'

        # Extract the link
        l = t.find('a') if t else None
        link = "https://amazon.in" + l["href"] if l else 'N/A'

        # Extract the price
        p = soup.find('span', attrs={"class": "a-price-whole"})
        price = p.get_text() if p else 'N/A'

        # Extract the rating
        r = soup.find('span', attrs={"class": "a-icon-alt"})
        rating = r.get_text() if r else 'N/A'

        # Append to the dictionary
        d["title"].append(title)
        d["rating"].append(rating)
        d["price"].append(price)
        d["link"].append(link)

    except Exception as e:
        print(e)

# Create a DataFrame and save to a CSV file
df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False)
