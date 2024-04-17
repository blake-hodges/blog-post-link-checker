import requests
from bs4 import BeautifulSoup

#change the url to the webpage you want to get the links from
url = "https://blog.pragmaticengineer.com/italian-bank-outage/"

response = requests.get(url)

#use the beautiful soup html parser
soup = BeautifulSoup(response.text, 'html.parser')

#save all the links from the webpage
links = soup.find_all('a')

#loop through the links and print to the console
for link in links:
    href = link.get('href')
    print(href)