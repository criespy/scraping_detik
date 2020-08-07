import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class':'grid-row list-content'})

judul = populer_area.findAll(attrs={'class':'media__title'})
gambar = populer_area.findAll(attrs={'class':'media__image'})

for j in judul:
    print(j.text)
for g in gambar:
    print(g.find('a').find('img')['title'])

#print(populer_area)