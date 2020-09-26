import csv
from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Firefox()
records = []
# URL pra pesquisar no google
url = 'https://www.google.com/search?q=covid-19&lr=lang_pt&tbs=cdr:1,cd_min:2/13/2020,cd_max:3/18/2020'

driver.get(url)
soup = bs(driver.page_source, 'html.parser')
result_list = soup.find('div', {'id': 'rso'}).findChildren(recursive=False)

def extract_records():
    first_result = result_list[0]
    second_result = result_list[1]

    records.append((first_result.h3.span.text, first_result.a.get('href')))
    records.append((second_result.h3.span.text, second_result.a.get('href')))

    return records


extract_records()

driver.close()

with open('searchResults.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Result Title', 'Result Link'])
    writer.writerows(records)
