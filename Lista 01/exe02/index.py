from selenium import webdriver

driver = webdriver.Firefox()
url = 'https://www.amazon.com/-/pt/dp/0132350882/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2LCJX22UGQAB7&dchild=1&keywords=clean+code&qid=1600991315&sprefix=clean+code%2Caps%2C270&sr=8-1'
driver.get(url)
bookTitle = driver.find_element_by_xpath(
    '//*[@id="productTitle"]')
bookAuthor = driver.find_element_by_xpath(
    '//*[@id="bylineInfo"]/span/span[1]/a[1]')
bookPrice = driver.find_element_by_xpath('//*[@id="newBuyBoxPrice"]')

f = open('mytestfile.txt', 'w')
f.write('Book Title: ' + bookTitle.text +' \n')
f.write('Book Author: ' + bookAuthor.text +' \n')
f.write('Book Price: ' + bookPrice.text +' \n')
f.close()

pass
