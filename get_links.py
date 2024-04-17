import requests
from bs4 import BeautifulSoup

#change the url to the webpage you want to get the links from
url = "https://blog.pragmaticengineer.com/italian-bank-outage/"

response = requests.get(url)

if response.status_code == 200:
    #use the beautiful soup html parser
    soup = BeautifulSoup(response.text, 'html.parser')

    #only search the content of the page (in this case, only use the element with id of content)
    content = soup.find(attrs={'id':'content'})
    links = soup.find_all('a')

    #loop through the links and print to the console
    for link in links:
        href = link.get('href')
        print(href)
else:
    print("failed to retrieve the webpage")