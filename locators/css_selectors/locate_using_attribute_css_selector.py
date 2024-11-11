from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')

# Approach #1: locating username input element using one attribute.
# username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')

# Approach #2: locating username input element using multiple attributes.
username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"][type="text"]')

# Quiting the driver.
driver.quit()
