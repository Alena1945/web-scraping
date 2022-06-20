import requests
import bs4

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1003991302.1644676271; hl=ru; fl=ru; _ym_uid=1644676271872899062; _ym_d=1644676271; _fbp=fb.1.1648059100890.108151185; visited_articles=498452:94230:315264:564826; __gads=ID=ffe82e89c8a3243b-22ff8e6ab5cd00ce:T=1644676273:S=ALNI_MZ9bBKFNXp5xj4G_zRyTgAhHlc2AQ; habr_web_home_feed=/all/; _ym_isad=2; _gid=GA1.2.1656486941.1655726008; __gpi=UID=00000533c97c2c96:T=1650812310:RT=1655726011:S=ALNI_MbpR8afu7mFlp_r0XoWvfR3gfBPsw',
    'Host': 'habr.com',
    'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Yandex";v="22"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.1.985 Yowser/2.5 Safari/537.36'
}

base_url = 'https://habr.com/ru/all/'
response = requests.get(base_url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')
for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = set(hub.find('span').text for hub in hubs)
    date = article.find('time').text
    title = article.find('a', class_='tm-article-snippet__title-link')
    span_title = title.find('span').text
    # print(span_title)
    if KEYWORDS & hubs:
        href = title['href']
        url = 'https://habr.com' + href
        print(f'Дата: {date} - Заголовок: {span_title} - Ссылка: {url}')


