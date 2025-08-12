from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Optional: Prevent browser from opening visibly
options = Options()
options.add_argument("--headless")  # Run in background
driver = webdriver.Chrome(options=options)  # You must have ChromeDriver in PATH

# Open the website
url = "https://www.worldometers.info/world-population/population-by-country/"
driver.get(url)
time.sleep(5)  # Wait for page to load

# Parse page using BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Scrape the correct table
table = soup.find("table")  # First table on the page (no need for ID)

# Extract headers
headers = [th.text.strip() for th in table.find_all("th")]

# Extract rows
rows = []
for tr in table.tbody.find_all("tr"):
    cols = [td.text.strip().replace(",", "") for td in tr.find_all("td")]
    rows.append(cols)

# Convert to DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save to CSV
df.to_csv("population_data.csv", index=False)
print("✅ Data saved to population_data.csv")
