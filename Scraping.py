# # import requests
# # from bs4 import BeautifulSoup
# # import pandas as pd
# #
# # # Send a GET request to the website
# # url = 'https://www.w3schools.com/html/html_tables.asp'
# # response = requests.get(url)
# #
# # # Parse the HTML content of the webpage
# # soup = BeautifulSoup(response.text, 'html.parser')
# #
# # # Find the table you want to scrape
# # table = soup.find('table', {'id': 'customers'})
# #
# # # Extract the table headers
# # headers = [header.text for header in table.find_all('th')]
# #
# # # Extract the table rows
# # rows = []
# # for row in table.find_all('tr')[1:]:
# #     rows.append([val.text for val in row.find_all('td')])
# #
# # # Create a Pandas DataFrame
# # df = pd.DataFrame(rows, columns=headers)
# #
# # # Print the DataFrame
# # print(df)
# #
# #
# #
#
#
# import requests
# from bs4 import BeautifulSoup
#
# # Send a GET request to the website
# url = 'https://www.subexpert.com/'
# response = requests.get(url)
#
# # Parse the HTML content of the webpage
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Extract the HTML content
# html_content = soup.prettify()
#
# # Print the HTML content
# print(html_content)
#

# scraping data from Fiverr
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import random
#
# def get_proxies():
#     # Replace these with actual proxy URLs
#     proxies = [
#         'http://192.99.169.19',
#         'http://132.145.50.210',
#         # Add more proxy types as needed
#     ]
#     return proxies
#
# def scrape_fiverr(keyword, num_pages=200):
#     base_url = 'https://www.fiverr.com/search/gigs?query={}'.format(keyword)
#     gig_data = []
#
#     user_agents = [
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         # Add more user-agents as needed
#     ]
#
#     proxies = get_proxies()
#
#     for page in range(1, num_pages + 1):
#         page_url = '{}&page={}'.format(base_url, page)
#
#         headers = {'User-Agent': random.choice(user_agents)}
#         proxy = {'http': random.choice(proxies), 'https': random.choice(proxies)}
#
#         try:
#             response = requests.get(page_url, headers=headers, proxies=proxy)
#             response.raise_for_status()
#
#             soup = BeautifulSoup(response.text, 'html.parser')
#             gigs = soup.find_all('div', class_='gig-wrapper')
#
#             for gig in gigs:
#                 title = gig.find('h3', class_='gig-title').text.strip()
#                 username = gig.find('span', class_='gig-seller-info__username').text.strip()
#
#                 gig_data.append({'Title': title, 'Username': username})
#
#         except requests.exceptions.RequestException as e:
#             print("Failed to fetch data for page {}. Error: {}".format(page, e))
#
#         time.sleep(1)  # Add a delay of 1 second between requests to avoid rate limits
#
#     return gig_data
#
# def save_to_excel(data, file_name='fiverr_gigs.xlsx'):
#     df = pd.DataFrame(data)
#     df.to_excel(file_name, index=False)
#     print('Data saved to {}'.format(file_name))
#
# if __name__ == "__main__":
#     keyword = 'web scraping'
#     num_pages = 200
#     gig_data = scrape_fiverr(keyword, num_pages)
#
#     if gig_data:
#         save_to_excel(gig_data)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scrape_fiverr(keyword, num_pages=200):
    base_url = 'https://www.fiverr.com/search/gigs?query={}'.format(keyword)
    gig_data = []

    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        # Add more user-agents as needed
    ]

    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without UI)

    for page in range(1, num_pages + 1):
        page_url = '{}&page={}'.format(base_url, page)

        headers = {'User-Agent': random.choice(user_agents)}

        try:
            # Use Selenium to execute JavaScript
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(page_url)
            time.sleep(2)  # Wait for JavaScript to execute (adjust as needed)

            # Get the page source after JavaScript execution
            page_source = driver.page_source
            driver.quit()

            soup = BeautifulSoup(page_source, 'html.parser')
            gigs = soup.find_all('div', class_='gig-wrapper')

            for gig in gigs:
                title_element = gig.find('h3', class_='gig-title')
                if title_element:
                    title = title_element.text.strip()
                else:
                    title = 'Title not available'

                username_element = gig.find('span', class_='gig-seller-info__username')
                if username_element:
                    username = username_element.text.strip()
                else:
                    username = 'Username not available'

                gig_data.append({'Title': title, 'Username': username})

        except Exception as e:
            print("Failed to fetch data for page {}. Error: {}".format(page, e))

        time.sleep(2)  # Add a delay of 2 seconds between requests to avoid rate limits

    return gig_data

def save_to_excel(data, file_name='fiverr_gigs.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)
    print('Data saved to {}'.format(file_name))

if __name__ == "__main__":
    keyword = 'web scraping'
    num_pages = 200
    gig_data = scrape_fiverr(keyword, num_pages)

    if gig_data:
        save_to_excel(gig_data)
