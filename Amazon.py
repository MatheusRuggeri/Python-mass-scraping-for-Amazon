"""
===========
A basic mass web scraper to Amazon in Python.

@author: Matheus Ruggeri
===========
"""

from bs4 import BeautifulSoup 
import requests

# You need a user agent to avoid Amazon recognize you as a robot.
# Go to google.com -> my user agent -> copy your agent and paste.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

# In the main function we will create a dict with product's ID and which amazon store is selling it.
# This code allows you to scrape from the following Amazon stores: Brazil, Germany and USA.
# The product's ID is in the URL: https://www.amazon.com/dp/B082TJT44G -> B082TJT44G -> Echo Dot.
def main():
    products = {"B00NHQF6MG": "BR"}			# A Lego set in Brazilian store
    products.update({"B07QGKVY8D": "BR"})		# A shoe with a range price ('R$49,90 - R$129,58')
    products.update({"B07PHPXHQS": "DE"})		# An Echo Dot in German store
    products.update({"B00FLYWNYQ": "USA"})		# An Instant Pot in USA store
    scrape(products) 
	
# The scrape function will get the product's ID and which Amazon store is it listed.
def scrape(products):
    for (ID, country) in products.items():
        if country.upper() == "BR":
            domain = "com.br"
        elif country.upper() == "DE":
            domain = "de"
        elif country.upper() == "USA":
            domain = "com"
        else:
            domain = "com"
    
	# Concat the values to get the URL to the product
        url = "https://www.amazon." + domain + "/dp/" + ID
	# Request the page using the URL, the headers that was defined in the beggining and LXML, a third-party Python parser (you might install lxml)
        soup = BeautifulSoup(requests.get(url, headers=headers).content, 'lxml')
    
	# Find the product's Title and Amazon's price
        title = soup.find(id='productTitle')
        price = soup.find(id='priceblock_ourprice')
        
	# To return a human readable text, you should use get_text(), a method from BeautifulSoup, I suggest you print the values before and after get_text() to see the differeces.
        title = (title.get_text(strip=True))
        price = (price.get_text(strip=True))
		
	# Print your data
        data = {'Product':title, 'Price':price} 
        print(data)
  
main()