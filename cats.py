import requests
import re
import random


def get_cats(i):
    if i == 'gif':
        r = requests.get('http://thecatapi.com/api/images/get?format=html&type=gif')
        match = re.search(r'src=[\'"]?([^\'" >]+)', r.text)
        return match.group(0)[5:]
    else:
        i = random.randrange(1, 10)
        if i == 8:
            i = i - 1
        url = 'https://api.thecatapi.com/v1/images/search?category_ids={}'.format(i)
        json_data = requests.get(url).json()
        return json_data[0]['url']
