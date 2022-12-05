import requests
import random
from bs4 import BeautifulSoup

def download_img(url, name):
    print(url)
    img = requests.get(url)
    with open(name, 'wb') as f: 
        f.write(img.content)


url = 'https://unsplash.com/s/photos/keyboards'
req = requests.get(url).text
bs = BeautifulSoup(req, "html.parser")

imgs = bs.find("div", {"class": "mItv1"}).findAll("img")

for i in range(4):
    download_img(random.choice(imgs)["src"], f"image{i}.jpeg")