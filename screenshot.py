from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
import time

s = Service("C:/Users/MANU/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Create ChromeOptions and set incognito mode
chrome_options = Options()
chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--disable-javascript')
# chrome_options.add_argument('--headless')  # for headless browsing

driver = webdriver.Chrome(service=s, options = chrome_options)

webUrl = "https://www.nastygal.com/gb/womens/sale?home_promosplash_all-sale"
driver.get(webUrl)

# Set a maximum number of scroll attempts to avoid an infinite loop
max_scroll_attempts = 10
scroll_attempt = 0

# Scroll to the bottom of the page
while scroll_attempt < max_scroll_attempts:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    scroll_attempt += 1
    time.sleep(1)  # Optional: Add a delay to allow content to load

# Take a screenshot
# driver.save_screenshot("C:/Users/MANU/Pictures/just-try.png")

# Quit the WebDriver
driver.quit()
