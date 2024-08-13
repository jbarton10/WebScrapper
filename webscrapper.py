import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://hackthissite.org')
results=[]
content=driver.page_source
soup=BeautifulSoup(content, 'html.parser')