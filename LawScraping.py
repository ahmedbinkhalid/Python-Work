import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://mangaseek.net/"

# Send a GET request to the URL with SSL certificate verification disabled
response = requests.get(url, verify=False)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all text on the page
    all_text = soup.get_text()

    # Print all the text
    print(all_text)
else:
    print("Failed to retrieve website content.")
