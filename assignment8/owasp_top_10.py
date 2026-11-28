# Task 6: Scraping Structured Data

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://owasp.org/Top10/2025/")

# Find the 10 vulnerabilities using XPath
risks = driver.find_elements(
    By.XPATH, '//h3[@id="top-102025-list"]/following-sibling::ol[1]/li/a'
)

# Store the vulnerability titles and links
results = []

for risk in risks:
    results.append({
        "Title": risk.text,
        "Link": risk.get_attribute("href")
    })

# Print the results
for result in results:
    print(result)

driver.quit()

# Task 6: Save the OWASP Top 10 results to a CSV file
with open("assignment8/owasp_top_10.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Link"])
    writer.writeheader()
    writer.writerows(results)

print("CSV file saved successfully!")