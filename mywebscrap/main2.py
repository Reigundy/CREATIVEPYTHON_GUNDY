import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Ada_Lovelace")
# print(response.text)

soup = bs4.BeautifulSoup(response.text, "html.parser")

images = soup.select('img')
print(images)

image_links = []
for img in soup.select('img'):
    src = img.get("src")
    print(src)
    image_links.append(f"https:{src}")
   # image_links.append("https:" + src)

print(image_links)

import urllib.request
from urllib.error import HTTPError

for index, tem in enumerate(image_links):
    file_name = "img_" + str(index) +".jpg"
    file_path = "images/"
    full_path = '{}{}'.format(file_path, file_name)
    #Can pair two strings together to compact inside the format function 
    #print(full_path)
    try:
        urllib.request.urlretrieve(img, full_path)
    except urllib.error.HTTPError as err:
        print(err.code)
        pass
