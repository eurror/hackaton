import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    html = requests.get(url).text
    return html


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars = soup.find_all('div', class_='list-item list-label')
    for item in cars:
        title = item.find('h2', class_='name').text.strip()
        price = item.find('strong').text.strip()
        description = ' '.join(item.find(
            'div', class_='block info-wrapper item-info-wrapper').text.split())
        image = item.find('img').get('data-src')
        data = {
            'title': title,
            'price': price,
            'description': description,
            'image': image,
        }
        write_to_csv([data['title'], data['price'], data['description'], data['image']])
    num = int(soup.find_all('li', class_='page-item')[-1].find('a').get('data-page'))
    return num


def write_to_csv(data):
    with open('cars.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def main():
    url = 'https://www.mashina.kg/search/all/'  # легковые автомобили
    page = '?page='
    html = get_html(url)
    num = get_data(html)
    for i in range(1, num+1):
        url_pages = url+page+str(i)
        html = get_html(url_pages)
        get_data(html)

main()
