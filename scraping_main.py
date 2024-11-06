###--- Это продолжение скрипта PyScraping_1
###--- Скрипт парсит информацию о товарах с заходом в каждую карточку
###--- Скрипт не содержит подробных комментариев из первой части


import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {
	"User-Agent":
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0"
	}

def get_url():
	for count in range(1, 7):
		url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
		response = requests.get(url, headers=headers)
		soup = BeautifulSoup(response.text, "lxml")
		data = soup.find_all("div", class_="w-full rounded border")

		for i in data:
			card_url ="https://scrapingclub.com" + i.find("a").get("href")
			yield card_url

for card_url in get_url():

	response = requests.get(card_url, headers=headers)
	sleep(3)
	soup = BeautifulSoup(response.text, "lxml")

	data = soup.find("div", class_="my-8 w-full rounded border")
	name = data.find("h3", class_="card-title").text
	price = data.find("h4", class_="my-4 card-price").text
	text = data.find("p", class_="card-description").text
	img_url = "https://scrapingclub.com" + data.find("img", class_="card-img-top").get("src")
	print(name + "\n" + price + "\n" + text + "\n" + img_url + "\n\n")