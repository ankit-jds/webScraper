from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

page = []
products = []
prices = []
brands = []
links = []
# driver.get("")
main_link = ""
for pageNo in range(1, 3):
    if (pageNo == 1):
        driver.get(main_link)
    else:
        driver.get(main_link+"&page="+str(pageNo))

    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('div', attrs={'class': '_1xHGtK _373qXS'}):

        page.append(pageNo)
        brand = a.find('div', attrs={'class': '_2WkVRV'})
        name = a.find('a', attrs={'class': 'IRpwTa'})
        price = a.find('div', attrs={'class': '_30jeq3'})
        link = a.find('a', attrs={'class': '_2UzuFa'})

        print(brand.text, name.text, price.text, link.get('href'))
        if(brand and price and name and link):
            products.append(name.text)
            prices.append(price.text)
            brands.append(brand.text)
            links.append(main_link+link.get('href'))
            print(name.text, price.text, brand.text)

    print(products, prices, brands)
    print(len(products), len(prices), len(brands))
df = pd.DataFrame(
    {'Page': page, 'Brand': brands, 'Product Name': products, 'Price': prices, "Links": links})
df.to_csv('products.csv', index=False, encoding='utf-8')
