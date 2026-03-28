# ---------------- SELENIUM TEST (selenium_test.py) ----------------

# Install:
# pip install selenium
# Download ChromeDriver and add to PATH

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup driver
driver = webdriver.Chrome()
driver.get('file:///YOUR_PATH/index.html')

# Test success
driver.find_element(By.ID, 'username').send_keys('admin')
driver.find_element(By.ID, 'password').send_keys('1234')
driver.find_element(By.TAG_NAME, 'button').click()

time.sleep(1)
print('Success Test:', driver.find_element(By.ID, 'result').text)

# Reset

driver.refresh()

# Test failure
driver.find_element(By.ID, 'username').send_keys('user')
driver.find_element(By.ID, 'password').send_keys('wrong')
driver.find_element(By.TAG_NAME, 'button').click()

time.sleep(1)
print('Failure Test:', driver.find_element(By.ID, 'result').text)

driver.quit()
