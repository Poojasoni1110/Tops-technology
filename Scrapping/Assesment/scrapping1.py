# Import required libraries
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

service = Service("msedgedriver.exe")

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Edge(service=service, options=options)
wait = WebDriverWait(driver, 20)

url = "http://quotes.toscrape.com"
driver.get(url)

wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

soup = BeautifulSoup(driver.page_source, "html.parser")

quotes = soup.find_all("div", class_="quote")

quote_list = []
author_list = []
tag_list = []

for q in quotes:
    quote_text = q.find("span", class_="text").text
    author = q.find("small", class_="author").text
    tags = q.find_all("a", class_="tag")
    tag_values = [tag.text for tag in tags]

    quote_list.append(quote_text)
    author_list.append(author)
    tag_list.append(", ".join(tag_values))

time.sleep(8)
driver.quit()

data = pd.DataFrame({
    "Quote": quote_list,
    "Author": author_list,
    "Tags": tag_list
})

print(data)
data.to_csv("quotes_data.csv", index=False)

print("Web scraping completed and data saved successfully.")
