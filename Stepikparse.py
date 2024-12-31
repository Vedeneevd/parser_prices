import requests
from bs4 import BeautifulSoup
import lxml

with requests.Session() as session:
    total_prices = 0
    all_hrefs = []
    for index_page in range(1,6):
        for site_page in range(1,5):
            base_url = f'https://parsinger.ru/html/index{index_page}_page_{site_page}.html'
            response = session.get(base_url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            hrefs = soup.find_all('a',class_='name_item')
            for href in hrefs:
                href = href.get('href')
                all_hrefs.append(href)

    for item_href in all_hrefs:
            url = f'https://parsinger.ru/html/{item_href}'
            response = session.get(url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            counts = soup.find_all('span', id = 'in_stock')
            counts = [int(count.text.split()[-1]) for count in counts]

            prices = soup.find_all('span', id = "price")
            prices = [int(price.text.split()[0]) for price in prices]
            for count,price in zip(counts,prices):
                total_prices += count * price
    print(total_prices)










    #     for j in range(33):
    #         mouse_url = f'https://parsinger.ru/html/mouse/3/3_{j}.html'
    #         response = session.get(mouse_url)
    #         response.encoding = 'utf-8'
    #         soup = BeautifulSoup(response.text, 'lxml')
    #         articles = soup.find_all('p', class_ = 'article')
    #         for article in articles:
    #             article = int(article.text.split()[-1])
    #
    #             total_article.append(article)
    # print(sum(total_article))

