import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

# List of URLs to scrape
urls = [
    "https://mangaseek.net/person/list/a.html",
    "https://mangaseek.net/person/list/ka.html",
    "https://mangaseek.net/person/list/sa.html",
    "https://mangaseek.net/person/list/ku.html",
    "https://mangaseek.net/person/list/he.html",
    "https://mangaseek.net/person/list/yo.html",
    "https://mangaseek.net/person/list/ko.html",
    "https://mangaseek.net/person/list/so.html",
    "https://mangaseek.net/person/list/no.html",
    "https://mangaseek.net/person/list/ru.html",
    "https://mangaseek.net/person/list/wa.html",
    "https://mangaseek.net/person/list/e.html",
    "https://mangaseek.net/person/list/u.html",
    "https://mangaseek.net/person/list/ne.html",
    "https://mangaseek.net/person/list/ta.html",
    "https://mangaseek.net/person/list/na.html",
    "https://mangaseek.net/person/list/ha.html",
    "https://mangaseek.net/person/list/ma.html",
    "https://mangaseek.net/person/list/ya.html",
    "https://mangaseek.net/person/list/ra.html",
    "https://mangaseek.net/person/list/i.html",
    "https://mangaseek.net/person/list/ki.html",
    "https://mangaseek.net/person/list/shi.html",
    "https://mangaseek.net/person/list/chi.html",
    "https://mangaseek.net/person/list/ni.html",
    "https://mangaseek.net/person/list/hi.html",
    "https://mangaseek.net/person/list/mi.html",
    "https://mangaseek.net/person/list/ri.html",
    "https://mangaseek.net/person/list/tsu.html",
    "https://mangaseek.net/person/list/mu.html",
    "https://mangaseek.net/person/list/n.html",
    "https://mangaseek.net/person/list/ke.html",
    "https://mangaseek.net/person/list/se.html",
    "https://mangaseek.net/person/list/mo.html",
]

# Maximum number of rows to scrape
MAX_ROWS = 20000

# List to hold all the scraped data
data = []

# Iterate over each URL
for url in urls:
    if len(data) >= MAX_ROWS:
        break

    print(f"Fetching URL: {url}")
    retries = 3
    initial_response = None
    for attempt in range(retries):
        try:
            # Send a request to the URL and get the HTML content
            initial_response = requests.get(url, timeout=10)
            initial_response.raise_for_status()  # Raise an exception for HTTP errors
            break
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            if attempt < retries - 1:
                print(f"Retrying... ({attempt + 1}/{retries})")
                time.sleep(2)
            else:
                print(f"Failed to fetch {url} after {retries} attempts.")
                initial_response = None

    if not initial_response:
        print(f"Skipping URL due to failure: {url}")
        continue

    html_content = initial_response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the table containing the person data
    table = soup.find("table", {"id": "person"})

    if not table:
        print(f"No table found on URL: {url}")
        continue

    # Iterate over the table rows
    for row in table.find_all("tr")[1:]:
        if len(data) >= MAX_ROWS:
            break

        # Extract the person ID and person name from the row
        person_id = row.find("span", {"class": "badge-person"}).text
        person_name = row.find("a").text.strip()

        # Get the URL of the person's detail page
        detail_page_url = "https://mangaseek.net" + row.find("a")["href"]

        # Retry mechanism and error handling for detail pages
        detail_page_html = None
        for attempt in range(retries):
            try:
                # Send a request to the detail page URL and get the HTML content
                detail_page_response = requests.get(detail_page_url, timeout=10)
                detail_page_response.raise_for_status()  # Raise an exception for HTTP errors
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

        # Extract additional information from the detail page
        alternate_name = detail_page_soup.find("meta", {"itemprop": "alternateName"})
        alternate_name = alternate_name["content"] if alternate_name else ""

        occupation = detail_page_soup.find("td", {"itemprop": "jobTitle"})
        occupation = occupation.text if occupation else ""

        nationality = ""
        birth_date = ""
        hometown = ""
        debut = ""
        awards = ""
        affiliation = ""
        hobbies = ""
        website = ""
        twitter = ""
        facebook = ""
        blog = ""
        pixiv = ""
        source = ""
        initial_contributor = ""
        last_updated_by = ""

        rows = detail_page_soup.find_all("tr")
        for r in rows:
            heading = r.find("th")
            if heading:
                heading_text = heading.text.strip()
                if "国籍" in heading_text:
                    nationality = r.find("td").text.strip()
                elif "生年月日" in heading_text:
                    birth_date = r.find("td").text.strip()
                elif "出身地" in heading_text:
                    hometown = r.find("td").text.strip()
                elif "デビュー" in heading_text:
                    debut = r.find("td").text.strip()
                elif "受賞" in heading_text:
                    awards = ", ".join([award.text.strip() for award in r.find_all("li")])
                elif "所属" in heading_text:
                    affiliation = r.find("td").text.strip()
                elif "趣味" in heading_text:
                    hobbies = r.find("td").text.strip()
                elif "公式サイト" in heading_text:
                    website_tag = r.find("a")
                    website = website_tag["href"] if website_tag else ""
                elif "Twitter" in heading_text:
                    twitter_tag = r.find("a")
                    twitter = twitter_tag["href"] if twitter_tag else ""
                elif "Facebook" in heading_text:
                    facebook_tag = r.find("a")
                    facebook = facebook_tag["href"] if facebook_tag else ""
                elif "ブログ" in heading_text:
                    blog_tag = r.find("a")
                    blog = blog_tag["href"] if blog_tag else ""
                elif "Pixiv" in heading_text:
                    pixiv_tag = r.find("a")
                    pixiv = pixiv_tag["href"] if pixiv_tag else ""
                elif "出典" in heading_text:
                    source = r.find("td").text.strip()
                elif "初投稿者" in heading_text:
                    initial_contributor = r.find("td").text.strip()
                elif "最終更新者" in heading_text:
                    last_updated_by = r.find("td").text.strip()

        # Append the data to the list
        data.append([person_id, person_name, alternate_name, occupation, nationality, birth_date, hometown, debut, awards, affiliation, hobbies, website, twitter, facebook, blog, pixiv, source, initial_contributor, last_updated_by])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=["Person ID", "Person Name", "Alternate Name", "Occupation", "Nationality", "Birth Date", "Hometown", "Debut", "Awards", "Affiliation", "Hobbies", "Website", "Twitter", "Facebook", "Blog", "Pixiv", "Source", "Initial Contributor", "Last Updated By"])

# Save the DataFrame to an Excel file
df.to_excel("Person_list(full-japanese).xlsx", index=False)

print("Data scraping completed. Results saved to Person_list(full-japanese).xlsx")
