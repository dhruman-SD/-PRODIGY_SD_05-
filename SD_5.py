import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.jumia.co.ke/mlp-black-friday/phones-tablets/?page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
products = soup.find_all('article', class_='prd _fb col c-prd')
names = []
prices = []
ratings = []
for product in products:
    name = product.find('h3', class_='name').text
    names.append(name)
    price = product.find('div', class_='prc').text
    prices.append(price)
    rating = product.find('div', class_='rev').find('div', class_='stars _s').text
    ratings.append(rating)
df = pd.DataFrame({'Product Name': names, 'Price': prices, 'Rating': ratings})
df.to_csv('product_data.csv', index=False, encoding='utf-8')
print("Product data extracted and saved to product_data.csv")
