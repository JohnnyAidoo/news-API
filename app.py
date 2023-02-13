import requests
from bs4 import BeautifulSoup
from flask import Flask

json = {}

link = 'https://news.google.com/home?hl=en-GH&gl=GH&ceid=GH:en'
req = requests.get(link)

soup = BeautifulSoup(req.content, 'html.parser')

finder = soup.find("a", class_ ='WwrzSb')
img_finder = soup.find('img', class_='Quavad')


for text,img in zip(finder,img_finder):
    head = (text['arial-label'])
    print(head)
    url_link = (text['href'])
    print(url)
    print(img['srcset'])
print('done')