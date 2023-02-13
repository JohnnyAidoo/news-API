import requests
from bs4 import BeautifulSoup
from flask import Flask
import json

jsonObject = {}

link = 'https://news.google.com/home?hl=en-GH&gl=GH&ceid=GH:en'
req = requests.get(link)

soup = BeautifulSoup(req.content, 'html.parser')

finder = soup.find_all("a", class_ ='WwrzSb')
img_finder = soup.find_all('img', class_='Quavad')


for text,img in zip(finder,img_finder):
    head = (text['aria-label'])
#    print(head)
    url_link = (text['href'])
#    print(url_link)
    url_image = (img['srcset'])
#    print(url_image)

print('done')

json.dump(jsonObject)