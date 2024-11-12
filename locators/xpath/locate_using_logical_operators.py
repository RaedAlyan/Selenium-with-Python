from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.letskodeit.com/practice')

# locating using and logical operator
open_tab_button = driver.find_element(By.XPATH, '//a[@id="opentab" and @class="btn-style class1 class2"]')
open_tab_button.click()

# locating using or logical operator
disable_button = driver.find_element(By.XPATH, '//input[@id="disabled-button" or @value="disable"]')
disable_button.click()

# locating using not logical operator
disable_button = driver.find_element(By.XPATH, '//input[not(@value="Enable")]')
disable_button.click()
driver.quit()
