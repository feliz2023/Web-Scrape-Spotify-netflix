# Netflix Scrape

# 1. FILLING A FORM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the webdriver
driver = webdriver.Edge()

url = "https://www.netflix.com/in/login"
driver.get(url)

# Find the input fields by its ID
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_userLoginId"))
)
pass_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_password"))
)

# Fill in the input field with an email or phone number and password
email_field.send_keys("your email")
pass_field.send_keys("your password")

time.sleep(1)

# Sign in Automation
sign_in_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-submit"))
)

sign_in_button.click()

time.sleep(10)

# sign out
partial_link_text = "Sign out of Netflix"

driver.get("https://help.netflix.com/en/")

element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "signout-link"))
)
# signout_link = driver.find_element(By.CLASS_NAME, "signout-link")
element.click()
time.sleep(10)

# Close the browser window
driver.quit()
