from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')

# Approach #1: locating the login button using the class CSS selector.
# login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')

# Approach #2: locating the login button using the class CSS selector.
# login_button = driver.find_element(By.CSS_SELECTOR, '.radius')

# Approach #3: locating the login button using the class CSS selector.
login_button = driver.find_element(By.CSS_SELECTOR, 'button[class="radius"]')

# Clicking on the login button.
login_button.click()

# Quiting the driver.
driver.quit()
