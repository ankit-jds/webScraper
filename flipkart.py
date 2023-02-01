from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products = []
prices = []
ratings = []

# driver.get("")

# mobile phones
driver.get("")
# driver.get("")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):

    name = a.find('div', attrs={'class': '_4rR01T'})
    price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    rating = a.find('div', attrs={'class': '_3LWZlK'})
    print(name.text, price.text)
    if(rating and price and name):
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)
        print(name.text, price.text, rating.text)

print(products,prices,ratings)
print(len(products),len(prices),len(ratings))
df = pd.DataFrame(
    {'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('phones.csv', index=False, encoding='utf-8')
