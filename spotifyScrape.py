from selenium import webdriver
# from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# initialize the driver
driver = webdriver.Edge()

url = "https://www.spotify.com/in-en/account/overview/?utm_source=spotify&utm_medium=menu&utm_campaign=your_account"
driver.get(url)

# id and pass
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-username"))
)
pass_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-password"))
)

# Fill in the input field with an email or phone number and password
email_field.send_keys("your email")
pass_field.send_keys("your password")

time.sleep(1)
# remember me part unchecked
# Find the indicator element
indicator = driver.find_element(By.CLASS_NAME, "Indicator-sc-acu4qz-0")

# Click the indicator to toggle the checkbox
indicator.click()

time.sleep(1)

# login automation
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-button"))
)

login_button.click()
time.sleep(10)

# CLICK THE EDIT PROFILE LINK
# Find the element by its attributes
# Scroll down to make the element visible
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

edit_profile_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Edit profile'))
)
edit_profile_link.click()
time.sleep(5)

# Find the dropdown element
dropdown_element = driver.find_element(By.CLASS_NAME, "SelectContainer-sc-wv4dj5-0")

# Click on the dropdown to open it
dropdown_element.click()
time.sleep(2)

# Now, select "Male" by clicking the corresponding option
male_option = driver.find_element(By.XPATH, '//option[@value="FEMALE"]')
male_option.click()
time.sleep(3)

# SAVE PROFILE
save_profile_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
save_profile_button.click()
time.sleep(5)

# Close the browser window
driver.quit()
