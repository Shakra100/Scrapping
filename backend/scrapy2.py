import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
#
import json

# Open the JSON file
def query(file):
  with open(file) as f:
      data = json.load(f)
      return data
# Print the data (it will be stored as a Python dictionary)
user_queries=query('/query.json')
print(user_queries)

# Function to extract Product Title
def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        title_value = title.text.strip()
    except AttributeError:
        title_value = ""
    return title_value

# Function to extract Product Price
def get_price(soup):
    try:
        price_whole= soup.find("span", attrs={'class': 'a-price-whole'}).text.strip()
        price_decimal = soup.find("span", attrs={'class': "a-price-fraction"}).text.strip()
        price= price_whole + price_decimal
    except AttributeError:
        price = "Not Available"
    return price

# Function to extract Product Rating
def get_rating(soup):
    try:    
        rating = soup.find("span", attrs={'class': "a-icon-alt"}).text.strip()
        
    except AttributeError:
        rating = "Not Rated"
    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).text.strip()
    except AttributeError:
        review_count = "No Reviews"
    return review_count

# Function to extract Product Rating
def get_url(soup):
    try:
       # Find the div with id 'imgTagWrapperId'
        img_div = soup.find('div', id='imgTagWrapperId')

        # Find the <img> tag inside the div
        img_tag = img_div.find('img')

        image_url = img_tag['src']
    except AttributeError:
        image_url = "Not Found"
    return image_url



# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'}).find("span").text.strip()
    except AttributeError:
        available = "Not Available"
    return available

# Function to extract Availability Status
def get_sales(soup):
    try:
        sales = soup.find("span", attrs={'id': 'social-proofing-faceout-title-tk_bought'}).find("span").text.strip()
    except AttributeError:
        sales = "Not Available"
    return sales




# Add your User-Agent
HEADERS = ({'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'})

# Base URL
BASE_URL = "https://www.amazon.com/"



for user_query in user_queries:
    # Data storage
    d = {"title": [], "price": [], "rating": [], "reviews": [], "availability": [], "sales": [], "image_url":[]}
    URL = f"{BASE_URL}s?k={user_query}"
    print(URL)
        # Loop through the first 10 pages
    for page in range(1, 11):
        print(f"Scraping page {page}...")
        # Append the page number to the URL
        Query_URL = f"{URL}&page={page}"
        print("User query URL", Query_URL)
        webpage = requests.get(Query_URL, headers=HEADERS)
        #print("Requested Webpage", webpage)
        soup = BeautifulSoup(webpage.content, "html.parser")
        #print(soup)
        
        # Fetch links to product pages
        links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})
        links_list = [link.get('href') for link in links]
        #print("LINKS", links)
        #print("LINKLISTS",links_list)

        # Extract details from each product link
        for link in links_list:
            new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
            #print("WebPage Text",new_webpage.text)
            new_soup = BeautifulSoup(new_webpage.content, "html.parser")
            #print("new_soup")

            d['title'].append(get_title(new_soup))
            print(d['title'])
            d['price'].append(get_price(new_soup))
            d['rating'].append(get_rating(new_soup))
            d['reviews'].append(get_review_count(new_soup))
            d['availability'].append(get_availability(new_soup))
            d['sales'].append(get_sales(new_soup))
            d['image_url'].append(get_url(new_soup))
        
    
        # Create a DataFrame
    amazon_df = pd.DataFrame.from_dict(d)
        # Clean and save the data
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df.dropna(subset=['title'], inplace=True)
        # File name for storing JSON
    file_name = f"{user_query}.json"

    # Save the JSON with square brackets using orient='records' and lines=False
    json_data = amazon_df.to_json(orient='records', lines=False)

    # Wrap the output in square brackets manually
    with open(file_name, 'w') as f:
        f.write(f"{json_data}")




print("Data scraping completed and saved in json format")
