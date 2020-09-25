from selenium import webdriver
from bs4 import BeautifulSoup as bs
import csv

driver = webdriver.Firefox()
records = []
def buscar_produto(produto):
    url = get_url(produto)
    driver.get(url)

def get_url(produto):
    termo_busca = produto.replace(' ', '+')
    url = 'https://www.amazon.com/s?k={}'
    return url.format(termo_busca)

def extract_record(item):
    prod_name_tag = item.h2.a
    price_tag = item.find('span', {'class':'a-offscreen'})
    rating_tag = item.find('span', {'class': 'a-icon-alt'})
    prod_name = prod_name_tag.text.strip()
    try:
        prod_price = price_tag.text.strip()
    except AttributeError:
        prod_price = ''
    try:
        prod_rating = rating_tag.text.strip()
    except AttributeError:
        prod_rating = ''

    return (prod_name, prod_price, prod_rating)

def extract_prod_list():
    soup = bs(driver.page_source, 'html.parser')
    return soup.find_all('div', {'data-component-type':'s-search-result'})


def create_records_list(results):
    for result in results:
        record = extract_record(result)
        if record:
            records.append(record)    

buscar_produto('monitor LG')
results = extract_prod_list()
create_records_list(results)

driver.close()

with open('amazon_prods.csv', 'w', newline = '', encoding = 'utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Product Name', 'Product Price', 'Product Rating'])
    writer.writerows(records)

