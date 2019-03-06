import requests


def weather(latitude, longitude):

    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&' \
          'appid=ff4138355d772de3d5e02734eea46925'.format(latitude, longitude)
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.65'
    }

    session = requests.Session()
    ask = session.get(url, headers=headers)
    if ask.status_code == 404:
        return 'Возникли какие-то проблемы😱'

    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    degrees = int(temp - 273.15)
    a = ""
    if degrees <= 0:
        a = a + ('Temperature : ' + str(degrees) + '°' + "❄\n")
    elif degrees < 10:
        a = a + ('Temperature : ' + str(degrees) + '°' + ' 👌\n')
    elif degrees > 10:
        a = ('Temperature : ' + str(degrees) + '°' + '☀\n')
    a = a + ('Wind speed 🌬️: {} м/с'.format(wind_speed) + '\n' + 'Description📜:' + data['weather'][0]['description'])
    return a
