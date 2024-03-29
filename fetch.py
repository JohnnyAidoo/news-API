import requests
from bs4 import BeautifulSoup
import json

JsonObject = {}
array = []

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
    JsonObject.update({"head":head, "url": url_link, "image":url_image})
    array.append(JsonObject)
data = json.dumps(array)

print('done')
