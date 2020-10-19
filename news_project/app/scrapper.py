import requests
from bs4 import BeautifulSoup
from .models import News


def news_scrap(data):
    """call particular scrapping function base on key"""

    for key, value in data.items():
        if key == 'Washington Post':
            washington(key, value)
        elif key == 'CNN':
            cnn(key, value)
        elif key == 'Time':
            times(key, value)
        elif key == 'QZ':
            qz(key, value)
        elif key == 'Slashdot':
            slashdot(key, value)
    return None


def washington(name, url):
    """scrap data from web page and store in database"""

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_data = soup.find_all('div', {'class': 'card-top card-text'})
    for i in all_data:
        try:
            detail = i.find('div', {'class': 'bb pb-xs font--subhead 1h-fronts-sm font-light gray-dark'}).get_text()
            title = i.find('span').get_text()
            news_object = News(Title=title, Details=detail, NewsFrom=name, URL='https://www.washingtonpost.com/')
            news_object.save()
        except:
            print('scraping error or data repeat')
    return None


def cnn(name, url):
    pass


def times(name, url):
    pass


def qz(name, url):
    pass


def slashdot(name, url):
    pass
