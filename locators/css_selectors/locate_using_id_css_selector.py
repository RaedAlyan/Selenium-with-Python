from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')

# Approach #1: locating the username input element using the ID CSS selector.
# username_input = driver.find_element(By.CSS_SELECTOR, '#username')

# Approach #2: locating the username input element using the ID CSS selector.
# username_input = driver.find_element(By.CSS_SELECTOR, 'input#username')

# Approach #3: locating the username input element using the ID CSS selector.
username_input = driver.find_element(By.CSS_SELECTOR, 'input[id="username"]')

# Sending the specified key to the username input element.
username_input.send_keys('Raed')

# Quiting the driver.
driver.quit()
