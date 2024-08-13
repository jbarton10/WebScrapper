import requests
from bs4 import BeautifulSoup


url = 'https://hackthissite.org'


response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)


