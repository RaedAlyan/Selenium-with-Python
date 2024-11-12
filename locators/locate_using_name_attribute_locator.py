from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')

# locating username input using the name attribute locator
username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys('Raed Eleyan')
driver.quit()
