import requests
from bs4 import BeautifulSoup

url = "https://blog.pragmaticengineer.com/italian-bank-outage/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    print(href)