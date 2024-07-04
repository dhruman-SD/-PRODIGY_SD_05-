import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the e-commerce website
url = "https://www.jumia.co.ke/mlp-black-friday/phones-tablets/?page=1"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')

# Find all product articles on the page
products = soup.find_all('article', class_='prd _fb col c-prd')

# Initialize lists to store product information
names = []
prices = []
ratings = []

# Loop through each product article
for product in products:
    # Extract product name
    name = product.find('h3', class_='name').text
    names.append(name)

    # Extract product price
    price = product.find('div', class_='prc').text
    prices.append(price)

    # Extract product rating
    rating = product.find('div', class_='rev').find('div', class_='stars _s').text
    ratings.append(rating)

# Create a Pandas DataFrame to store the product information
df = pd.DataFrame({'Product Name': names, 'Price': prices, 'Rating': ratings})

# Save the DataFrame to a CSV file
df.to_csv('product_data.csv', index=False, encoding='utf-8')

print("Product data extracted and saved to product_data.csv")
