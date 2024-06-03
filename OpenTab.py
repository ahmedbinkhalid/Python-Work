

# import undetected_chromedriver as webdriver
# import time
# import getpass
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
# # Delay for demonstration purposes
# time.sleep(10)
#
# # Close the browser
# driver.quit()

import undetected_chromedriver as webdriver
import time
import getpass

options = webdriver.ChromeOptions()
username = getpass.getuser()
path = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.add_argument(f"--user-data-dir={path}")

driver = webdriver.Chrome(options=options, use_subprocess=True)
driver.get("https://myaccount.google.com/")

# Wait for page to load
time.sleep(5)

# Find and click the "Go to Google Account" button by its text
try:
    go_to_account_button = driver.find_element(by='link text', value="Go to Google Account")
    go_to_account_button.click()
    print("Clicked 'Go to Google Account' button")
except Exception as e:
    print("Failed to click 'Go to Google Account' button:", e)

# Wait for the page to load
time.sleep(5)

# Find and click the "Sign in" link on the Google Account page
try:
    sign_in_link = driver.find_element(by='link text', value="Sign in")
    sign_in_link.click()
    print("Clicked 'Sign in' link")
except Exception as e:
    print("Failed to click 'Sign in' link:", e)

# Wait for the page to load
time.sleep(5)

# Find the email input field and enter the email
try:
    email_input = driver.find_element(by='xpath', value="//input[@id='identifierId']")
    email_input.send_keys("mainishqorrdard@gmail.com")
    print("Entered email")
except Exception as e:
    print("Failed to enter email:", e)

# Find and click the "Next" button
try:
    next_button = driver.find_element(by='xpath', value="//button[@id='identifierNext']")
    next_button.click()
    print("Clicked 'Next' button")
except Exception as e:
    print("Failed to click 'Next' button:", e)

# Delay for demonstration purposes
time.sleep(10)

# Close the browser
driver.quit()




