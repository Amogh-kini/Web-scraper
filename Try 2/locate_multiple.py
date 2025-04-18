# pip install selenium.
# Tut in selenium in python.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#==============================================================================================================================================================================

query="laptop"
i=1
amazon_url = f"https://www.amazon.in/s?k={query}&page={i}&crid=212TW4JYFJ6EJ&sprefix=laptop%2Caps%2C205&ref=nb_sb_noss_2"

#==============================================================================================================================================================================

driver = webdriver.Chrome()
URL = amazon_url
driver.get(URL)
elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")

#==============================================================================================================================================================================

print(f"{len(elems)} items found !")
print(" ")

#==============================================================================================================================================================================

file=1
for elem in elems:
    fetch = elem.get_attribute("outerHTML")
    with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
        f.write(fetch)
        file+=1
    time.sleep(3)

driver.close()


# one single laptop has one html file.