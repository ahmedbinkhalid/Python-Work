# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
# # Send a GET request to the website
# url = 'https://www.w3schools.com/html/html_tables.asp'
# response = requests.get(url)
#
# # Parse the HTML content of the webpage
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Find the table you want to scrape
# table = soup.find('table', {'id': 'customers'})
#
# # Extract the table headers
# headers = [header.text for header in table.find_all('th')]
#
# # Extract the table rows
# rows = []
# for row in table.find_all('tr')[1:]:
#     rows.append([val.text for val in row.find_all('td')])
#
# # Create a Pandas DataFrame
# df = pd.DataFrame(rows, columns=headers)
#
# # Print the DataFrame
# print(df)
#
#
#


import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://www.subexpert.com/'
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the HTML content
html_content = soup.prettify()

# Print the HTML content
print(html_content)

