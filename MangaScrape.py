# import requests
# from bs4 import BeautifulSoup
# import csv
# import re
# import time
#
# # List of URLs to scrape
# urls = [
#     "https://mangaseek.net/person/list/ta.html",
#     "https://mangaseek.net/person/list/na.html",
#     "https://mangaseek.net/person/list/ha.html",
#     "https://mangaseek.net/person/list/ma.html",
#     "https://mangaseek.net/person/list/ya.html",
#     "https://mangaseek.net/person/list/ra.html",
#     "https://mangaseek.net/person/list/i.html",
#     "https://mangaseek.net/person/list/ki.html",
#     "https://mangaseek.net/person/list/shi.html",
#     "https://mangaseek.net/person/list/chi.html",
#     "https://mangaseek.net/person/list/ni.html",
#     "https://mangaseek.net/person/list/hi.html",
#     "https://mangaseek.net/person/list/mi.html",
#     "https://mangaseek.net/person/list/ri.html",
#     "https://mangaseek.net/person/list/tsu.html",
#     "https://mangaseek.net/person/list/mu.html",
#     "https://mangaseek.net/person/list/n.html",
#     "https://mangaseek.net/person/list/ke.html",
#     "https://mangaseek.net/person/list/se.html",
#     "https://mangaseek.net/person/list/mo.html",
# ]
#
# # Open a CSV file for writing
# with open("Manga(3)_data.csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#
#     # Write the header row
#     writer.writerow(["Person ID", "Person Name", "Alternate Name", "Occupation", "Nationality", "Birth Date", "Hometown", "Debut", "Awards", "Affiliation", "Hobbies", "Website", "Twitter", "Facebook", "Blog", "Pixiv", "Source", "Initial Contributor", "Last Updated By"])
#
#     # Iterate over each URL
#     for url in urls:
#         print(f"Fetching URL: {url}")
#         retries = 3
#         initial_response = None
#         for attempt in range(retries):
#             try:
#                 # Send a request to the URL and get the HTML content
#                 initial_response = requests.get(url, timeout=10)
#                 initial_response.raise_for_status()  # Raise an exception for HTTP errors
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Error fetching {url}: {e}")
#                 if attempt < retries - 1:
#                     print(f"Retrying... ({attempt + 1}/{retries})")
#                     time.sleep(2)
#                 else:
#                     print(f"Failed to fetch {url} after {retries} attempts.")
#                     initial_response = None
#
#         if not initial_response:
#             print(f"Skipping URL due to failure: {url}")
#             continue
#
#         html_content = initial_response.content
#
#         # Parse the HTML content with BeautifulSoup
#         soup = BeautifulSoup(html_content, "html.parser")
#
#         # Find the table containing the person data
#         table = soup.find("table", {"id": "person"})
#
#         if not table:
#             print(f"No table found on URL: {url}")
#             continue
#
#         # Iterate over the table rows
#         for row in table.find_all("tr")[1:]:
#             # Extract the person ID and person name from the row
#             person_id = row.find("span", {"class": "badge-person"}).text
#             person_name = row.find("a").text.strip()
#
#             # Get the URL of the person's detail page
#             detail_page_url = "https://mangaseek.net" + row.find("a")["href"]
#
#             # Retry mechanism and error handling for detail pages
#             detail_page_html = None
#             for attempt in range(retries):
#                 try:
#                     # Send a request to the detail page URL and get the HTML content
#                     detail_page_response = requests.get(detail_page_url, timeout=10)
#                     detail_page_response.raise_for_status()  # Raise an exception for HTTP errors
#                     detail_page_html = detail_page_response.content
#                     break
#                 except requests.exceptions.RequestException as e:
#                     print(f"Error fetching {detail_page_url}: {e}")
#                     if attempt < retries - 1:
#                         print(f"Retrying... ({attempt + 1}/{retries})")
#                         time.sleep(2)
#                     else:
#                         print(f"Failed to fetch {detail_page_url} after {retries} attempts. Skipping.")
#
#             if not detail_page_html:
#                 continue
#
#             # Parse the detail page HTML content with BeautifulSoup
#             detail_page_soup = BeautifulSoup(detail_page_html, "html.parser")
#
#             # Extract additional information from the detail page
#             alternate_name = detail_page_soup.find("meta", {"itemprop": "alternateName"})
#             alternate_name = alternate_name["content"] if alternate_name else ""
#
#             occupation = detail_page_soup.find("td", {"itemprop": "jobTitle"})
#             occupation = occupation.text if occupation else ""
#
#             nationality = ""
#             birth_date = ""
#             hometown = ""
#             debut = ""
#             awards = ""
#             affiliation = ""
#             hobbies = ""
#             website = ""
#             twitter = ""
#             facebook = ""
#             blog = ""
#             pixiv = ""
#             source = ""
#             initial_contributor = ""
#             last_updated_by = ""
#
#             rows = detail_page_soup.find_all("tr")
#             for r in rows:
#                 heading = r.find("th")
#                 if heading:
#                     heading_text = heading.text.strip()
#                     if "国籍" in heading_text:
#                         nationality = r.find("td").text.strip()
#                     elif "生年月日" in heading_text:
#                         birth_date = r.find("td").text.strip()
#                     elif "出身地" in heading_text:
#                         hometown = r.find("td").text.strip()
#                     elif "デビュー" in heading_text:
#                         debut = r.find("td").text.strip()
#                     elif "受賞" in heading_text:
#                         awards = ", ".join([award.text.strip() for award in r.find_all("li")])
#                     elif "所属" in heading_text:
#                         affiliation = r.find("td").text.strip()
#                     elif "趣味" in heading_text:
#                         hobbies = r.find("td").text.strip()
#                     elif "公式サイト" in heading_text:
#                         website_tag = r.find("a")
#                         website = website_tag["href"] if website_tag else ""
#                     elif "Twitter" in heading_text:
#                         twitter_tag = r.find("a")
#                         twitter = twitter_tag["href"] if twitter_tag else ""
#                     elif "Facebook" in heading_text:
#                         facebook_tag = r.find("a")
#                         facebook = facebook_tag["href"] if facebook_tag else ""
#                     elif "ブログ" in heading_text:
#                         blog_tag = r.find("a")
#                         blog = blog_tag["href"] if blog_tag else ""
#                     elif "Pixiv" in heading_text:
#                         pixiv_tag = r.find("a")
#                         pixiv = pixiv_tag["href"] if pixiv_tag else ""
#                     elif "出典" in heading_text:
#                         source = r.find("td").text.strip()
#                     elif "初投稿者" in heading_text:
#                         initial_contributor = r.find("td").text.strip()
#                     elif "最終更新者" in heading_text:
#                         last_updated_by = r.find("td").text.strip()
#
#             # Write the data to the CSV file
#             writer.writerow([person_id, person_name, alternate_name, occupation, nationality, birth_date, hometown, debut, awards, affiliation, hobbies, website, twitter, facebook, blog, pixiv, source, initial_contributor, last_updated_by])
#
# print("Data scraping completed. Results saved to person_data.csv")




# FOR WORK DATA




# import requests
# from bs4 import BeautifulSoup
# import csv
# import re
#
# # List of URLs to scrape
# urls = [
#     "https://mangaseek.net/work/list/a.html",
#     # Add more URLs for other pages
# ]
#
# # Open a CSV file for writing
# with open("work_data.csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#
#     # Write the header row
#     writer.writerow(["Work ID", "Title", "Thumbnail Picture", "Credit", "Year of First Publication", "First Publisher", "User Rating", "Reviews"])
#
#     # Iterate over each URL
#     for url in urls:
#         # Send a request to the URL and get the HTML content
#         response = requests.get(url)
#         html_content = response.content
#
#         # Parse the HTML content with BeautifulSoup
#         soup = BeautifulSoup(html_content, "html.parser")
#
#         # Find the table containing the work data
#         table = soup.find("table", {"id": "work"})
#
#         # Iterate over the table rows
#         for row in table.find_all("tr")[1:]:
#             # Extract the work ID and title from the row
#             work_id = row.find("span", {"class": "badge badge-work"}).text
#             title = row.find("a").text.strip()
#
#             # Get the URL of the work's detail page
#             detail_page_url = "https://mangaseek.net" + row.find("a")["href"]
#
#             # Send a request to the detail page URL and get the HTML content
#             detail_page_response = requests.get(detail_page_url)
#             detail_page_html = detail_page_response.content
#
#             # Parse the detail page HTML content with BeautifulSoup
#             detail_page_soup = BeautifulSoup(detail_page_html, "html.parser")
#
#             # Extract additional information from the detail page
#             thumbnail_picture = detail_page_soup.find("img", {"itemprop": "image"})["src"] if detail_page_soup.find("img", {"itemprop": "image"}) else ""
#             credit = ", ".join([author.text.strip() for author in detail_page_soup.find_all("a", {"itemprop": "author"})])
#             year_of_first_publication = detail_page_soup.find("td", text=re.compile("初版年")).next_sibling.text.strip() if detail_page_soup.find("td", text=re.compile("初版年")) else ""
#             first_publisher = detail_page_soup.find("td", text=re.compile("出版社")).next_sibling.text.strip() if detail_page_soup.find("td", text=re.compile("出版社")) else ""
#
#             user_rating = detail_page_soup.find("strong", text=re.compile("平均評価は")).next_sibling.strip() if detail_page_soup.find("strong", text=re.compile("平均評価は")) else ""
#             reviews = detail_page_soup.find("strong", text=re.compile("のレビューが投稿されています。")).previous_sibling.strip() if detail_page_soup.find("strong", text=re.compile("のレビューが投稿されています。")) else ""
#
#             # Write the data to the CSV file
#             writer.writerow([work_id, title, thumbnail_picture, credit, year_of_first_publication, first_publisher, user_rating, reviews])
#
# print("Data scraping completed. Results saved to work_data.csv")

# import requests
# from bs4 import BeautifulSoup
# import csv
# import re
#
# # List of URLs to scrape
# urls = [
#     "https://mangaseek.net/work/list/a.html",
#     # Add more URLs for other pages
# ]
#
# # Open a CSV file for writing
# with open("work_data.csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#
#     # Write the header row
#     writer.writerow(["Work ID", "Title", "Thumbnail Picture", "Credit", "Year of First Publication", "First Publisher", "User Rating", "Reviews"])
#
#     # Iterate over each URL
#     for url in urls:
#         # Send a request to the URL and get the HTML content
#         response = requests.get(url)
#         html_content = response.content
#
#         # Parse the HTML content with BeautifulSoup
#         soup = BeautifulSoup(html_content, "html.parser")
#
#         # Find the table containing the work data
#         table = soup.find("table", {"id": "work"})
#
#         # Iterate over the table rows
#         for row in table.find_all("tr")[1:]:
#             # Extract the work ID and title from the row
#             work_id = row.find("span", {"class": "badge badge-work"}).text
#             title = row.find("a").text.strip()
#
#             # Get the URL of the work's detail page
#             detail_page_url = "https://mangaseek.net" + row.find("a")["href"]
#
#             # Send a request to the detail page URL and get the HTML content
#             detail_page_response = requests.get(detail_page_url)
#             detail_page_html = detail_page_response.content
#
#             # Parse the detail page HTML content with BeautifulSoup
#             detail_page_soup = BeautifulSoup(detail_page_html, "html.parser")
#
#             # Extract additional information from the detail page
#             thumbnail_picture = detail_page_soup.find("img", {"itemprop": "image"})["src"] if detail_page_soup.find("img", {"itemprop": "image"}) else ""
#             credit = ", ".join([author.text.strip() for author in detail_page_soup.find_all("a", {"itemprop": "author"})])
#             year_of_first_publication = detail_page_soup.find("td", string=re.compile("初版年")).next_sibling.text.strip() if detail_page_soup.find("td", string=re.compile("初版年")) else ""
#             first_publisher = detail_page_soup.find("td", string=re.compile("出版社")).next_sibling.text.strip() if detail_page_soup.find("td", string=re.compile("出版社")) else ""
#             user_rating = detail_page_soup.find("strong", string=re.compile("平均評価は")).next_sibling.strip() if detail_page_soup.find("strong", string=re.compile("平均評価は")) else ""
#             reviews = detail_page_soup.find("strong", string=re.compile("のレビューが投稿されています。")).previous_sibling.strip() if detail_page_soup.find("strong", string=re.compile("のレビューが投稿されています。")) else ""
#
#             # Write the data to the CSV file
#             writer.writerow([work_id, title, thumbnail_picture, credit, year_of_first_publication, first_publisher, user_rating, reviews])
#
# print("Data scraping completed. Results saved to work_data.csv")

# Final Code for Work list

# import requests
# from bs4 import BeautifulSoup
# import csv
# import re
# import time
#
# # Function to scrape data from a URL
# def scrape_data_from_url(url):
#     # Initialize a list to store the scraped data
#     scraped_data = []
#
#     retries = 3
#     initial_response = None
#     for attempt in range(retries):
#         try:
#             # Send a request to the URL and get the HTML content
#             initial_response = requests.get(url, timeout=10)
#             initial_response.raise_for_status()  # Raise an exception for HTTP errors
#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching {url}: {e}")
#             if attempt < retries - 1:
#                 print(f"Retrying... ({attempt + 1}/{retries})")
#                 time.sleep(2)
#             else:
#                 print(f"Failed to fetch {url} after {retries} attempts.")
#                 return []
#
#     if not initial_response:
#         print(f"Skipping URL due to failure: {url}")
#         return []
#
#     html_content = initial_response.content
#
#     # Parse the HTML content with BeautifulSoup
#     soup = BeautifulSoup(html_content, "html.parser")
#
#     # Find the table containing the work data
#     table = soup.find("table", {"id": "work"})
#
#     if not table:
#         print(f"No table found on URL: {url}")
#         return []
#
#     # Iterate over the table rows
#     for row in table.find_all("tr")[1:]:
#         # Extract the work ID and title from the row
#         work_id = row.find("span", {"class": "badge badge-work"}).text
#         title = row.find("a").text.strip()
#
#         # Get the URL of the work's detail page
#         detail_page_url = "https://mangaseek.net" + row.find("a")["href"]
#
#         # Retry mechanism and error handling for detail pages
#         detail_page_html = None
#         for attempt in range(retries):
#             try:
#                 # Send a request to the detail page URL and get the HTML content
#                 detail_page_response = requests.get(detail_page_url, timeout=10)
#                 detail_page_response.raise_for_status()  # Raise an exception for HTTP errors
#                 detail_page_html = detail_page_response.content
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Error fetching {detail_page_url}: {e}")
#                 if attempt < retries - 1:
#                     print(f"Retrying... ({attempt + 1}/{retries})")
#                     time.sleep(2)
#                 else:
#                     print(f"Failed to fetch {detail_page_url} after {retries} attempts. Skipping.")
#
#         if not detail_page_html:
#             continue
#
#         # Parse the detail page HTML content with BeautifulSoup
#         detail_page_soup = BeautifulSoup(detail_page_html, "html.parser")
#
#         # Extract additional information from the detail page
#         thumbnail_picture = detail_page_soup.find("img", {"itemprop": "image"})["src"] if detail_page_soup.find("img", {"itemprop": "image"}) else ""
#         credit = ", ".join([author.text.strip() for author in detail_page_soup.find_all("a", {"itemprop": "author"})])
#         year_of_first_publication = detail_page_soup.find("td", string=re.compile("初版年")).next_sibling.text.strip() if detail_page_soup.find("td", string=re.compile("初版年")) else ""
#         first_publisher = detail_page_soup.find("td", string=re.compile("出版社")).next_sibling.text.strip() if detail_page_soup.find("td", string=re.compile("出版社")) else ""
#         user_rating = detail_page_soup.find("strong", string=re.compile("平均評価は")).next_sibling.strip() if detail_page_soup.find("strong", string=re.compile("平均評価は")) else ""
#         reviews = detail_page_soup.find("strong", string=re.compile("のレビューが投稿されています。")).previous_sibling.strip() if detail_page_soup.find("strong", string=re.compile("のレビューが投稿されています。")) else ""
#         genre = detail_page_soup.find("td", string=re.compile("ジャンル")).next_sibling.text.strip() if detail_page_soup.find("td", string=re.compile("ジャンル")) else ""
#         num_volumes = detail_page_soup.find("td", string=re.compile("巻数")).next_sibling.text.strip() if detail_page_soup.find("td", string=re.compile("巻数")) else ""
#         status = detail_page_soup.find("td", string=re.compile("状態")).next_sibling.text.strip() if detail_page_soup.find("td", string=re.compile("状態")) else ""
#
#         # Append the data to the list
#         scraped_data.append([work_id, title, thumbnail_picture, credit, year_of_first_publication, first_publisher, user_rating, reviews, genre, num_volumes, status])
#
#         # Check if we have collected 2000 entries, if so, break the loop
#         if len(scraped_data) >= 2000:
#             break
#
#     return scraped_data
#
# # List of URLs to scrape
# urls = [
#     "https://mangaseek.net/work/list/a.html",
#     # Add more URLs for other pages
# ]
#
# # Open a CSV file for writing
# with open("work_data(try).csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#
#     # Write the header row
#     writer.writerow(["Work ID", "Title", "Thumbnail Picture", "Credit", "Year of First Publication", "First Publisher", "User Rating", "Reviews", "Genre", "Number of Volumes", "Status"])
#
#     # Iterate over each URL
#     for url in urls:
#         print(f"Fetching URL: {url}")
#
#         # Scrape data from the URL
#         scraped_data = scrape_data_from_url(url)
#
#         # Write the scraped data to the CSV file
#         for data_row in scraped_data:
#             writer.writerow(data_row)
#
# print("Data scraping completed. Results saved to work_data.csv")

# import requests
# from bs4 import BeautifulSoup
# import csv
# import re
# import time
#
# # Function to scrape data from a URL
# def scrape_data_from_url(url):
#     # Initialize a list to store the scraped data
#     scraped_data = []
#
#     retries = 3
#     initial_response = None
#     for attempt in range(retries):
#         try:
#             # Send a request to the URL and get the HTML content
#             initial_response = requests.get(url, timeout=10)
#             initial_response.raise_for_status()  # Raise an exception for HTTP errors
#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching {url}: {e}")
#             if attempt < retries - 1:
#                 print(f"Retrying... ({attempt + 1}/{retries})")
#                 time.sleep(2)
#             else:
#                 print(f"Failed to fetch {url} after {retries} attempts.")
#                 return []
#
#     if not initial_response:
#         print(f"Skipping URL due to failure: {url}")
#         return []
#
#     html_content = initial_response.content
#
#     # Parse the HTML content with BeautifulSoup
#     soup = BeautifulSoup(html_content, "html.parser")
#
#     # Find the table containing the work data
#     table = soup.find("table", {"id": "work"})
#
#     if not table:
#         print(f"No table found on URL: {url}")
#         return []
#
#     # Iterate over the table rows
#     for row in table.find_all("tr")[1:]:
#         # Extract the work ID and title from the row
#         work_id = row.find("span", {"class": "badge badge-work"}).text
#         title = row.find("a").text.strip()
#
#         # Get the URL of the work's detail page
#         detail_page_url = "https://mangaseek.net" + row.find("a")["href"]
#
#         # Retry mechanism and error handling for detail pages
#         detail_page_html = None
#         for attempt in range(retries):
#             try:
#                 # Send a request to the detail page URL and get the HTML content
#                 detail_page_response = requests.get(detail_page_url, timeout=10)
#                 detail_page_response.raise_for_status()  # Raise an exception for HTTP errors
#                 detail_page_html = detail_page_response.content
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Error fetching {detail_page_url}: {e}")
#                 if attempt < retries - 1:
#                     print(f"Retrying... ({attempt + 1}/{retries})")
#                     time.sleep(2)
#                 else:
#                     print(f"Failed to fetch {detail_page_url} after {retries} attempts. Skipping.")
#
#         if not detail_page_html:
#             continue
#
#         # Parse the detail page HTML content with BeautifulSoup
#         detail_page_soup = BeautifulSoup(detail_page_html, "html.parser")
#
#         # Find all tables on the detail page
#         detail_tables = detail_page_soup.find_all("table")
#
#         # Initialize variables to store scraped data
#         scraped_row = [work_id, title]
#
#         # Extract data from each table
#         for detail_table in detail_tables:
#             rows = detail_table.find_all("tr")
#             for row in rows:
#                 cells = row.find_all(["td", "th"])
#                 for cell in cells:
#                     scraped_row.append(cell.text.strip())
#
#         # Append the data to the list
#         scraped_data.append(scraped_row)
#
#         # Check if we have collected 2000 entries, if so, break the loop
#         if len(scraped_data) >= 2000:
#             break
#
#     return scraped_data
#
# # List of URLs to scrape
# urls = [
#     "https://mangaseek.net/work/list/a.html",
#     "https://mangaseek.net/work/list/ka.html",
#     "https://mangaseek.net/work/list/i.html",
#     "https://mangaseek.net/work/list/ki.html",
#     "https://mangaseek.net/work/list/u.html",
#     "https://mangaseek.net/work/list/ku.html",
#     "https://mangaseek.net/work/list/e.html",
#     "https://mangaseek.net/work/list/ke.html",
#     "https://mangaseek.net/work/list/o.html",
#     "https://mangaseek.net/work/list/ko.html",
#     "https://mangaseek.net/work/list/sa.html",
#     "https://mangaseek.net/work/list/hu.html",
#     # Add more URLs for other pages
# ]
#
# # Open a CSV file for writing
# with open("work_data(all).csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#
#     # Iterate over each URL
#     for url in urls:
#         print(f"Fetching URL: {url}")
#
#         # Scrape data from the URL
#         scraped_data = scrape_data_from_url(url)
#
#         # Write the header row
#         writer.writerow(["Work ID", "Title"] + ["Data" + str(i) for i in range(1, len(scraped_data[0]))])
#
#         # Write the scraped data to the CSV file
#         for data_row in scraped_data:
#             writer.writerow(data_row)
#
# print("Data scraping completed. Results saved to work_data.csv")

# import requests
# from bs4 import BeautifulSoup
# import csv
# import time
#
# # Function to scrape data from a URL
# def scrape_data_from_url(url):
#     # Initialize a list to store the scraped data
#     scraped_data = []
#
#     retries = 3
#     initial_response = None
#     for attempt in range(retries):
#         try:
#             # Send a request to the URL and get the HTML content
#             initial_response = requests.get(url, timeout=10)
#             initial_response.raise_for_status()  # Raise an exception for HTTP errors
#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching {url}: {e}")
#             if attempt < retries - 1:
#                 print(f"Retrying... ({attempt + 1}/{retries})")
#                 time.sleep(2)
#             else:
#                 print(f"Failed to fetch {url} after {retries} attempts.")
#                 return []
#
#     if not initial_response:
#         print(f"Skipping URL due to failure: {url}")
#         return []
#
#     html_content = initial_response.content
#
#     # Parse the HTML content with BeautifulSoup
#     soup = BeautifulSoup(html_content, "html.parser")
#
#     # Find the table containing the person data
#     table = soup.find("table", {"id": "work"})
#     if not table:
#         print(f"No table found on URL: {url}")
#         return []
#
#     # Iterate over the table rows
#     for row in table.find_all("tr")[1:]:
#         # Extract the person ID and name from the row
#         person_id = row.find("span", {"class": "badge badge-work"}).text
#         person_name = row.find("a").text.strip()
#
#         print(f"Scraping person: {person_name} (ID: {person_id})")
#
#         # Get the URL of the person's detail page
#         detail_page_url = "https://mangaseek.net" + row.find("a")["href"]
#
#         # Scrape detail page for work data
#         work_data = scrape_work_data_from_detail_page(detail_page_url)
#
#         # If work data is available, add it to scraped_data along with person details
#         if work_data:
#             scraped_data.extend([[person_id, person_name] + work_row for work_row in work_data])
#         else:
#             # Skip to the next person if no table is found
#             continue
#
#         # Check the limit of 2000 entries per URL
#         if len(scraped_data) >= 20:
#             break
#
#     return scraped_data
#
# # Function to scrape work data from a detail page
# def scrape_work_data_from_detail_page(detail_page_url):
#     # Initialize a list to store the scraped data
#     scraped_data = []
#
#     retries = 3
#     detail_page_html = None
#     for attempt in range(retries):
#         try:
#             # Send a request to the detail page URL and get the HTML content
#             detail_page_response = requests.get(detail_page_url, timeout=10)
#             detail_page_response.raise_for_status()  # Raise an exception for HTTP errors
#             detail_page_html = detail_page_response.content
#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching {detail_page_url}: {e}")
#             if attempt < retries - 1:
#                 print(f"Retrying... ({attempt + 1}/{retries})")
#                 time.sleep(2)
#             else:
#                 print(f"Failed to fetch {detail_page_url} after {retries} attempts. Skipping.")
#
#     if not detail_page_html:
#         return []
#
#     # Parse the detail page HTML content with BeautifulSoup
#     detail_page_soup = BeautifulSoup(detail_page_html, "html.parser")
#
#     # Find the specified table on the detail page
#     works_table = detail_page_soup.find("table", {"id": "works"})
#     if not works_table:
#         print(f"No works table found on detail page: {detail_page_url}")
#         return []
#
#     # Extract data from the table
#     for work_row in works_table.find("tbody").find_all("tr"):
#         work_cells = work_row.find_all("td")
#         work_id = work_cells[0].text.strip()
#         work_title = work_cells[1].text.strip()
#         credit = work_cells[2].text.strip()
#         first_publish_year = work_cells[3].text.strip()
#         first_published_in = work_cells[4].text.strip()
#         evaluation = work_cells[5].text.strip()
#         reviews = work_cells[6].text.strip()
#
#         # Combine all data into one row
#         scraped_row = [work_id, work_title, credit, first_publish_year, first_published_in, evaluation, reviews]
#         # Append the data to the list
#         scraped_data.append(scraped_row)
#
#     return scraped_data
#
# # List of URLs to scrape
# urls = [
#     "https://mangaseek.net/person/list/a.html",
#     # Add more URLs for other pages
# ]
#
# # Open a CSV file for writing
# with open("work_data.csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#
#     # Write the header row
#     writer.writerow(["Person ID", "Person Name", "Work ID", "Work Title", "Credit (Different PN)", "First Publish Year", "First Published In", "Evaluation", "Reviews"])
#
#     # Iterate over each URL
#     for url in urls:
#         print(f"Fetching URL: {url}")
#
#         # Scrape data from the URL
#         scraped_data = scrape_data_from_url(url)
#
#         # Write the scraped data to the CSV file
#         for data_row in scraped_data:
#             writer.writerow(data_row)
#
#             # Check if we have reached the limit of 2000 entries per URL
#             if len(scraped_data) >= 20:
#                 break
#
# print("Data scraping completed. Results saved to work_data.csv")

# import requests
# from bs4 import BeautifulSoup
# import csv
# import time
#
# def scrape_data_from_url(url, max_persons_per_url):
#     scraped_data = []
#     retries = 3
#     persons_checked = 0
#
#     for attempt in range(retries):
#         try:
#             # Fetch the main page content
#             response = requests.get(url, timeout=10)
#             response.raise_for_status()
#             html_content = response.content
#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching {url}: {e}")
#             if attempt < retries - 1:
#                 print(f"Retrying... ({attempt + 1}/{retries})")
#                 time.sleep(2)
#             else:
#                 print(f"Failed to fetch {url} after {retries} attempts.")
#                 return scraped_data
#
#     soup = BeautifulSoup(html_content, "html.parser")
#     table = soup.find("table", {"id": "person"})
#
#     if not table:
#         print(f"No table found on URL: {url}")
#         return scraped_data
#
#     # Iterate over the table rows
#     for row in table.find_all("tr")[1:]:
#         detail_page_url = "https://mangaseek.net" + row.find("a")["href"]
#
#         # Retry mechanism and error handling for detail pages
#         detail_page_html = None
#         for attempt in range(retries):
#             try:
#                 detail_page_response = requests.get(detail_page_url, timeout=10)
#                 detail_page_response.raise_for_status()
#                 detail_page_html = detail_page_response.content
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Error fetching {detail_page_url}: {e}")
#                 if attempt < retries - 1:
#                     print(f"Retrying... ({attempt + 1}/{retries})")
#                     time.sleep(2)
#                 else:
#                     print(f"Failed to fetch {detail_page_url} after {retries} attempts. Skipping.")
#
#         if not detail_page_html:
#             continue
#
#         detail_page_soup = BeautifulSoup(detail_page_html, "html.parser")
#         works_table = detail_page_soup.find("table", {"id": "works"})
#
#         if works_table:
#             for work_row in works_table.find_all("tr")[1:]:
#                 cells = work_row.find_all("td")
#                 if len(cells) == 7:
#                     work_id = cells[0].text.strip()
#                     title = cells[1].text.strip()
#                     credit = cells[2].text.strip()
#                     publish_date = cells[3].text.strip()
#                     first_published_in = cells[4].text.strip()
#                     evaluation = cells[5].text.strip()
#                     reviews = cells[6].text.strip()
#                     scraped_data.append([work_id, title, credit, publish_date, first_published_in, evaluation, reviews])
#                 else:
#                     print(f"Invalid number of cells in the row: {len(cells)}")
#         else:
#             print(f"Works table not found on detail page.")
#
#         persons_checked += 1
#         if persons_checked >= max_persons_per_url:
#             return scraped_data
#
#     return scraped_data
#
# # List of URLs to scrape
# urls = [
#     "https://mangaseek.net/person/list/a.html",
#     # Add more URLs for other pages
# ]
#
# max_persons_per_url = 20
#
# with open("work_diff(PN).csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Work ID", "Title", "Credit (Different PN)", "Publish Date", "First Published In", "Evaluation", "Reviews"])
#
#     for url in urls:
#         print(f"Fetching URL: {url}")
#         scraped_data = scrape_data_from_url(url, max_persons_per_url)
#
#         for data_row in scraped_data:
#             writer.writerow(data_row)
#
# print("Data scraping completed. Results saved to work_diff(PN).csv")

# import requests
# from bs4 import BeautifulSoup
# import csv
#
# def scrape_data_from_url(url, max_persons_per_url):
#     scraped_data = []
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     table = soup.find("table", {"id": "person"})
#
#     if not table:
#         print(f"No table found on URL: {url}")
#
#     # Iterate over the table rows
#     for row in table.find_all("tr")[1:]:
#         detail_page_url = "https://mangaseek.net" + row.find("a")["href"]
#         detail_page_response = requests.get(detail_page_url)
#         detail_page_soup = BeautifulSoup(detail_page_response.content, "html.parser")
#         works_table = detail_page_soup.find("table", {"id": "works"})
#
#         if works_table:
#             for work_row in works_table.find_all("tr")[1:]:
#                 cells = work_row.find_all("td")
#                 if len(cells) == 7:
#                     scraped_data.append([cell.get_text().strip() for cell in cells])
#                 else:
#                     print(f"Skipping row with invalid number of cells: {len(cells)}")
#         else:
#             print(f"Works table not found on detail page: {detail_page_url}")
#
#         if len(scraped_data) >= max_persons_per_url:
#             break
#
#     return scraped_data
#
# # List of URLs to scrape
# urls = [
#     "https://mangaseek.net/person/list/a.html",
#     # Add more URLs for other pages
# ]
#
# max_persons_per_url = 20
#
# with open("work_diff(PN).csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Work ID", "Title", "Credit (Different PN)", "Publish Date", "First Published In", "Evaluation", "Reviews"])
#
#     for url in urls:
#         print(f"Fetching URL: {url}")
#         scraped_data = scrape_data_from_url(url, max_persons_per_url)
#
#         for data_row in scraped_data:
#             writer.writerow(data_row)
#
# print("Data scraping completed. Results saved to work_diff(PN).csv")
import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_data_from_url(url):
    scraped_data = []
    retries = 3

    # Retry mechanism for initial request
    initial_response = None
    for attempt in range(retries):
        try:
            initial_response = requests.get(url, timeout=10)
            initial_response.raise_for_status()
            break
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            if attempt < retries - 1:
                print(f"Retrying... ({attempt + 1}/{retries})")
                time.sleep(2)
            else:
                print(f"Failed to fetch {url} after {retries} attempts.")
                return []

    if not initial_response:
        print(f"Skipping URL due to failure: {url}")
        return []

    html_content = initial_response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the table containing the work data
    table = soup.find("table", {"id": "work"})

    if not table:
        print(f"No table found on URL: {url}")
        return []

    # Iterate over the table rows
    for row in table.find_all("tr")[1:]:
        # Get the URL of the work's detail page
        detail_page_url = "https://mangaseek.net" + row.find("a")["href"]

        # Retry mechanism for detail page request
        detail_page_html = None
        for attempt in range(retries):
            try:
                detail_page_response = requests.get(detail_page_url, timeout=10)
                detail_page_response.raise_for_status()
                detail_page_html = detail_page_response.content
                break
            except requests.exceptions.RequestException as e:
                print(f"Error fetching {detail_page_url}: {e}")
                if attempt < retries - 1:
                    print(f"Retrying... ({attempt + 1}/{retries})")
                    time.sleep(2)
                else:
                    print(f"Failed to fetch {detail_page_url} after {retries} attempts. Skipping.")

        if not detail_page_html:
            continue

        # Parse the detail page HTML content with BeautifulSoup
        detail_page_soup = BeautifulSoup(detail_page_html, "html.parser")

        # Find the table containing the work's detail
        detail_table = detail_page_soup.find("table", {"id": "works"})

        if not detail_table:
            print(f"No 'works' table found on detail page: {detail_page_url}")
            continue

        # Iterate over the rows in the detail table
        for detail_row in detail_table.find_all("tr")[1:]:
            # Extract data from each cell in the row
            cells = detail_row.find_all(["td", "th"])
            scraped_row = [cell.text.strip() for cell in cells]

            # Append the row to the scraped data
            scraped_data.append(scraped_row)

    return scraped_data

# List of URLs to scrape
urls = [
    "https://mangaseek.net/person/list/a.html",
    # Add more URLs for other pages
]

# Open a CSV file for writing
with open("work_diff(PN).csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    # Iterate over each URL
    for url in urls:
        print(f"Fetching URL: {url}")

        # Scrape data from the URL
        scraped_data = scrape_data_from_url(url)

        # Write the scraped data to the CSV file
        for data_row in scraped_data:
            writer.writerow(data_row)

print("Data scraping completed. Results saved to work_data(all).csv")
