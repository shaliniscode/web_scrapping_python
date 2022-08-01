from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


URL = "https://www.octoparse.com/product"
driver.get(URL)
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

heading =[]
body = []
results = soup.find(class_= "reqirement-wrap flex flex-column width1200")

job_elements = results.find("div", class_="flex flex-one reqirement-body")

title = job_elements.find_all("h3")
description = job_elements.find_all("p")


for item in title:
    heading.append(item.text)
for desc in description:
    body.append(desc.text)
df = pd.DataFrame({'Title':heading, 'Description':body})

print(df)

