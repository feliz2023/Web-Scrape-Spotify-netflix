# CLICKING A LINK
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Initialize the EdgeDriver
# driver = webdriver.Edge()
#
# # Open a website
# driver.get("https://aws.amazon.com/free/?trk=14a4002d-4936-4343-8211-b5a150ca592b&sc_channel=ps&ef_id=Cj0KCQjwhL6pBhDjARIsAGx8D59YVThHIKXSna2KTwM4y1VPNQENzzcJnj97X8rrUWEATjfFF_RjmNAaAnmVEALw_wcB:G:s&s_kwcid=AL!4422!3!453325184782!e!!g!!aws!10712784856!111477279771&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all")
#
# # Find the link by partial text match
# partial_link_text = "Sign up for Activate Today "
#
# # Wait for the element to be clickable (adjust the timeout as needed)
# element = WebDriverWait(driver, 35).until(
#     EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, partial_link_text))
# )
#
# element.click()
# time.sleep(16)
#
# # Close the browser window
# driver.quit()


# CODE TO PRINT A LINK FROM A WEBSITE

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Initialize the EdgeDriver
# driver = webdriver.Edge()
#
# # Open the website
# driver.get("https://aws.amazon.com/free/?trk=14a4002d-4936-4343-8211-b5a150ca592b&sc_channel=ps&ef_id=Cj0KCQjwhL6pBhDjARIsAGx8D59YVThHIKXSna2KTwM4y1VPNQENzzcJnj97X8rrUWEATjfFF_RjmNAaAnmVEALw_wcB:G:s&s_kwcid=AL!4422!3!453325184782!e!!g!!aws!10712784856!111477279771&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all")
#
# # Find the link by partial text match
# partial_link_text = "Sign up for Activate Today "
# element = driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)
#
# # Get the link's URL
# link_url = element.get_attribute("href")
#
# # Print the link URL
# print(link_url)
#
# # Close the browser window
# driver.quit()

# FILLING A FORM
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
#     EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Sign out of Netflix"))
#     EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "netflix.com/SignOut?lnkctr=mL") and contains(text(), "Sign out of Netflix")]'))
        EC.element_to_be_clickable((By.CLASS_NAME, "signout-link"))
)
# signout_link = driver.find_element(By.CLASS_NAME, "signout-link")
element.click()
time.sleep(10)

# Close the browser window
driver.quit()
