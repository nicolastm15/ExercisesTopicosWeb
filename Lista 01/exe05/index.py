import csv
from selenium import webdriver
from bs4 import BeautifulSoup as bs

def extract_url(search_term, lang_code, min_date, max_date):
    search_term = search_term.replace(' ', '+')
    url_template = 'https://www.google.com/search?q={}&lr=lang_{}&tbs=cdr:1,cd_min:{},cd_max:{}'
    return url_template.format(search_term,lang_code, min_date, max_date)

def extract_record(item):
    if (type(item) != 'NoneType'):
        return (item.h3.span.text, item.a.get('href'))

def create_records_list(result_list):
    records = []
    for result in result_list:
        record = extract_record(result)
        if record:
            records.append(record)
    return records

def create_file(file_name, records):
    with open(file_name + '.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Result Title', 'Result Link'])
        writer.writerows(records)

def main(search_term, lang_code, min_date, max_date, file_name):
    driver = webdriver.Firefox()
    records = []
    
    url = extract_url(search_term, lang_code, min_date, max_date)
    driver.get(url)
    soup = bs(driver.page_source, 'html.parser')
    result_list = soup.find('div', {'id': 'rso'}).findChildren(
        'div', recursive=False)

    records = create_records_list(result_list)

    driver.close()

    create_file(file_name, records)

