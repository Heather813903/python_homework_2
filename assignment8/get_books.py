# Task 3 - Extract book data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json

# Set up ChromeDriver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Open the Books to Scrape website
driver.get("https://books.toscrape.com/")

# Find all book listings
books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

# Check the number of books found
print(len(books))

# Create an empty list to store book data
results = []

# Loop through each book
for book in books:
    title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
    price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
    rating = book.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class")
    rating = rating.split()[1]

    book_data = {
        "Title": title,
        "Price": price,
        "Rating": rating
    }

    results.append(book_data)

# Close the browser
driver.quit()

# Create and print the DataFrame
df = pd.DataFrame(results)
print(df)

# Task 4 - Write out the data

# Save the DataFrame to a CSV file
df.to_csv("get_books.csv", index=False)

# Save the results list to a JSON file
with open("get_books.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)