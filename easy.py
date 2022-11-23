import requests
import csv
import time
from bs4 import BeautifulSoup


enter = 'https://enter.kg'

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    computers = soup.find_all('div', class_='row')
    for item in computers:
        title = item.find('span', class_='prouct_name').text
        price = item.find('span', class_='price').text
        image = enter + item.find('img').get('src')
        data = {'title': title, 'price': price, 'image': image}
        write_to_csv([data['title'], data['price'], data['image']])


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    num = int(soup.find('span', class_='vm-page-counter').text.split()[-1])
    return num

def write_to_csv(data):
    with open('computers.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def get_html(url):
    html = requests.get(url).text
    return html

def main():
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(url)
    get_data(html)
    num = get_total_pages(html)
    for i in range(1, num):
        new_url = f'{url}/results,{i}01-{i}00'
        new_html = get_html(new_url)
        get_data(new_html)


while True:
    main()
    time.sleep(3600)
