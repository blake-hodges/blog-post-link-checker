import requests
from bs4 import BeautifulSoup

#change the url to the webpage you want to get the links from
url = "https://realpython.com/python-or-operator/"

response = requests.get(url)

if response.status_code == 200:
    #use the beautiful soup html parser
    soup = BeautifulSoup(response.text, 'html.parser')

    #this is where we will save the future links array
    links = []

    #check if there is an element with the id of "content" on the page
    #if so only search the content of the page (in this case, only use the element with id of content)
    if soup.find(attrs={'id':'content'}):
        print("there is an element with the id of content")
        content = soup.find(attrs={'id':'content'})
        links = content.find_all('a')
    #check if there is an <article> or <main> element on the page
    #if so only search the content in the article or main element
    elif soup.find('article') or soup.find('main'):
        content = soup.find('article') or soup.find('main')
        links = content.find_all('a')
    #find all the links on the page
    else:
        links = soup.findAll('a')
    #loop through the links and print to the console
    for link in links:
        href = link.get('href')
        print(href)
else:
    print("failed to retrieve the webpage")