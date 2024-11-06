import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {
	"User-Agent":
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0"
	}


def main():
    get_url()
    get_data()


def get_url():
    for count in range(1, 8):

        url = f"https://quotes.toscrape.com/page/{count}/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="quote")

        for i in data:
            quote_url = "https://quotes.toscrape.com" + i.find("a").get("href")
            yield quote_url

def get_data():
    for quote_url in get_url():

        response = requests.get(quote_url, headers=headers)
        sleep(0)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="author-details")
        author = data.find("h3", class_="author-title").text
        author_born_date = data.find("span", class_="author-born-date").text
        author_born_place = data.find("span", class_="author-born-location").text.replace("in ", "")
        yield author, author_born_date, author_born_place


if __name__ == "__main__":
    main()










