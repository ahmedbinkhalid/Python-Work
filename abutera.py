#
# import undetected_chromedriver as webdriver
# import time
# import getpass
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# options = webdriver.ChromeOptions()
# username = getpass.getuser()
# path = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
# options.add_argument(f"--user-data-dir={path}")
#
# driver = webdriver.Chrome(options=options, use_subprocess=True)
# driver.get("https://myaccount.google.com/")
#
# # Wait for page to load
# time.sleep(5)
#
# # Find and click the "Go to Google Account" button by its text
# try:
#     go_to_account_button = driver.find_element(by='link text', value="Go to Google Account")
#     go_to_account_button.click()
#     print("Clicked 'Go to Google Account' button")
# except Exception as e:
#     print("Failed to click 'Go to Google Account' button:", e)
#
# # Wait for the page to load
# time.sleep(5)
#
#
#
# # Find the email input field and enter the email
# try:
#     email_input = driver.find_element(by='xpath', value="//input[@id='identifierId']")
#     email_input.send_keys("mainishqorrdard@gmail.com")
#     print("Entered email")
# except Exception as e:
#     print("Failed to enter email:", e)
#
# # Find and click the "Next" button by its class name
#
#
# try:
#     ActionChains(driver).send_keys(Keys.ENTER).perform()
#     print("Pressed Enter key")
# except Exception as e:
#     print("Failed to press Enter key:", e)
# # Wait for the next page to load
# try:
#     password_input = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//input[@type='password' and @name='Passwd']"))
#     )
#     password_input.send_keys("main42dard")
#     print("Entered password")
# except Exception as e:
#     print("Failed to enter password:", e)
#
# time.sleep(1)
# try:
#     ActionChains(driver).send_keys(Keys.ENTER).perform()
#     print("Pressed Enter key")
# except Exception as e:
#     print("Failed to press Enter key:", e)
#
# time.sleep(1)
# import random
# websites = [
#     "https://www.google.com",
#     "https://www.youtube.com",
#     "https://www.facebook.com",
#     "https://www.amazon.com",
#     "https://www.wikipedia.org",
#     "https://twitter.com",
#     "https://www.instagram.com",
#     "https://www.reddit.com",
#     "https://www.linkedin.com",
#     "https://www.netflix.com"
# ]
#
# # Configure Chrome options
# options = webdriver.ChromeOptions()
# username = getpass.getuser()
# path = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
# options.add_argument(f"--user-data-dir={path}")
#
# # Loop for 50 iterations
# for _ in range(50):
#     # Randomly select a website
#     website = random.choice(websites)
#
#     # Open Chrome browser
#     driver = webdriver.Chrome(options=options, use_subprocess=True)
#
#     # Navigate to the randomly selected website
#     driver.get(website)
#     print(f"Searching: {website}")
#
#     # Wait for some time (you can customize this based on your requirements)
#     time.sleep(random.randint(3, 8))
#
#     # Close the browser
#     driver.quit()
#     # Wait for 3 seconds before searching the next website
#     time.sleep(1)
#
#
#
# # Close the browser
# driver.quit()
#
#
# import undetected_chromedriver as webdriver
# import time
# import getpass
# from selenium.webdriver.common.keys import Keys
# import random
#
# options = webdriver.ChromeOptions()
# username = getpass.getuser()
# path = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
# options.add_argument(f"--user-data-dir={path}")
#
# # Open Chrome browser
# driver = webdriver.Chrome(options=options, use_subprocess=True)
# driver.get("https://myaccount.google.com/")
#
# # Wait for page to load
# time.sleep(5)
#
# # Find and click the "Go to Google Account" button by its text
# try:
#     go_to_account_button = driver.find_element(by='link text', value="Go to Google Account")
#     go_to_account_button.click()
#     print("Clicked 'Go to Google Account' button")
# except Exception as e:
#     print("Failed to click 'Go to Google Account' button:", e)
#
# # Wait for the page to load
# time.sleep(5)
#
# # Find the email input field and enter the email
# try:
#     email_input = driver.find_element(by='xpath', value="//input[@id='identifierId']")
#     email_input.send_keys("mainishqorrdard@gmail.com")
#     print("Entered email")
# except Exception as e:
#     print("Failed to enter email:", e)
#
# # Find and press Enter key to proceed to password input
# try:
#     email_input.send_keys(Keys.ENTER)
#     print("Pressed Enter key")
# except Exception as e:
#     print("Failed to press Enter key:", e)
#
# # Wait for the password input field to become visible
# password_input = None
# while password_input is None:
#     try:
#         password_input = driver.find_element(by='xpath', value="//input[@type='password' and @name='Passwd']")
#     except:
#         time.sleep(1)
#
# # Enter the password
# password_input.send_keys("your_password_here")
# print("Entered password")
#
# # Press Enter key to login
# password_input.send_keys(Keys.ENTER)
# print("Pressed Enter key to login")
#
# # Wait for the page to load after login
# time.sleep(5)
#
# # List of 10 most searched websites
# websites = [
#     "https://www.google.com",
#     "https://www.youtube.com",
#     "https://www.facebook.com",
#     "https://www.amazon.com",
#     "https://www.wikipedia.org",
#     "https://twitter.com",
#     "https://www.instagram.com",
#     "https://www.reddit.com",
#     "https://www.linkedin.com",
#     "https://www.netflix.com"
# ]
#
# # Loop for 50 iterations
# for _ in range(50):
#     # Randomly select a website
#     website = random.choice(websites)
#
#     # Navigate to the randomly selected website
#     driver.get(website)
#     print(f"Searching: {website}")
#
#     # Wait for some time (you can customize this based on your requirements)
#     time.sleep(random.randint(3, 8))
#
# # Close the browser
# driver.quit()
#
#
#
#
#
#
import undetected_chromedriver as webdriver
import time
import getpass
import random

# Create ChromeOptions object
options = webdriver.ChromeOptions()
username = getpass.getuser()
path = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.add_argument(f"--user-data-dir={path}")

# List of 10 most searched websites
websites = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.amazon.com",
    "https://www.wikipedia.org",
    "https://twitter.com",
    "https://www.instagram.com",
    "https://www.reddit.com",
    "https://www.linkedin.com",
    "https://www.netflix.com"
]

# Open Chrome browser
driver = webdriver.Chrome(options=options, use_subprocess=True)

# Loop for 50 iterations
for _ in range(50):
    # Randomly select a website
    website = random.choice(websites)

    # Open a new tab
    driver.execute_script("window.open();")

    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[-1])

    # Navigate to the randomly selected website
    driver.get(website)
    print(f"Searching: {website}")

    # Wait for some time (you can customize this based on your requirements)
    time.sleep(random.randint(3, 8))

# Close the browser
driver.quit()

