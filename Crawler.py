#-*- coding:utf-8 -*-


from urlparse import urljoin
import requests
import csv
from bs4 import BeautifulSoup

url = "http://km.58.com/chuzu/pn{page}"
page = 1

csv_file = open("house.csv","wb")
csv_writer = csv.writer(csv_file, delimiter=',')

while True:

    html = requests.get(url.format(page=page))
    soup = BeautifulSoup(html.text, 'lxml')

    house_list = soup.select("body > div.mainbox > div.main > div.content > div.listBox > ul > li")

    for house in house_list:
        try:
            house_title = house.select("div.des > h2 > a")[0].get_text().strip()
            house_url = house.select("div.des > h2 > a")[0].get('href')
            house_price = house.select("div.listliright > div.money > b")[0].get_text().strip()
            house_location = house.select("div.des > p.add > a")[0].get_text().strip()
            print house_title
            print house_url
            print house_price
            print house_location

            csv_writer.writerow([house_title, house_url, house_price, house_location])
        except:
            pass

    page += 1
    nextpage = soup.select('#bottom_ad_li > div.pager > a.next')
    if not nextpage:
        break

csv_file.close()

