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

driver.get("https://www.flipkart.com/ckf/czl/~cs-1zk8p4dgbr/pr?sid=ckf%2Cczl&collection-tab-name=Large+Screen+TVs-DT&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhcmdlIFNjcmVlbiBUVnMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=7.productCard.PMU_V2_3")
# driver.get("https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts")

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
df.to_csv('products.csv', index=False, encoding='utf-8')
