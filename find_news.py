import requests
from bs4 import BeautifulSoup as bs


def get_news(link):
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.65'
    }
    session = requests.Session()
    ask = session.get(link, headers=headers)
    soup = bs(ask.content, 'html.parser')
    a = ""
    if ask.status_code == 200:
        if link == 'https://ria.ru':
            divs = soup.find_all('div', attrs={'class': 'content', 'id': 'content'})
            for div in divs:
                url = div.find('a', attrs={'class': 'cell-main-photo__link'})['href']
                return url

        elif link == 'https://meduza.io':
            divs = soup.find_all('div', attrs={'class': 'TopicBlock-content'})
            for div in divs:
                url = div.find('a', attrs={'class': 'Link-root Link-isInBlockTitle'})['href']
                a = a + 'https://meduza.io/' + url + '\n'
                return a
        elif link == 'https://m.lenta.ru':
            divs = soup.find_all('div', attrs={'class': 'b-section'})
            for div in divs:
                url = div.find('a', attrs={'class': 'b-list-item__link'})['href']
                a = ('https://m.lenta.ru/' + url)
                return a

