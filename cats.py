import requests
from bs4 import BeautifulSoup as bs
import random


def cat():
    list = []
    kitty = []
    count = 0
    a = ""
    url = 'https://www.pexels.com/search/cat/'
    r = requests.get(url)
    html_content = r.text
    soup = bs(html_content, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        # print image source
        list.append(str(image['src']))
    for page in list:
        if page.find('/assets/') and page.find('https://images.pexels.com/users/avatars') and page.find('https://www.gravatar.com/avatar/9fd9cac0277d746907a8bf48d6797273?s=60&d=mm'):
            count += 1
            kitty.append(page)
    return kitty[random.randrange(0, count)]
"""
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.65'
    }
    session = requests.Session()
    ask = session.get(url, headers=headers)
    soup = bs(ask.content, 'lxml')
    divs = soup.find_all('div', attrs={'class': 'hide-featured-badge hide-photographer hide-favorite-badge'})

    for div in divs:
        a = div.find('a', attrs={'class': 'js-photo-link photo-item__link'})
        print("---------------------------------------------------------------------")
        print(a)

"""


