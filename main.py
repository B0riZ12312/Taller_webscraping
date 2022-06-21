from bs4 import BeautifulSoup
import requests
import unicodedata

# webpage url
url = 'https://www.ensenachile.cl/testimonios/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Encontrar todos los div que tienen class 'item-hito'
divs = soup.find_all('div', {'class':['col-md-6']})
for div in divs:
    print(div)