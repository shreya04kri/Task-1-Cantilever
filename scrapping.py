from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

output_dir = "data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

driver = webdriver.Chrome()
search='headphones'
file =0
for i in range (1,21):
    driver.get(f"https://www.amazon.in/s?k={search}&page={i}")

    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
    print(f"{len(elems)}items found")
    for elem in elems:
        d=elem.get_attribute("outerHTML")
        with open(f"{output_dir}/{search}_{file}.html","w", encoding="utf-8") as f:
            f.write(d)
            file +=1
time.sleep(2)
driver.close() #closes only the current window not the web driver where as quite() closes all