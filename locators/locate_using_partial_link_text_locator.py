from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.letskodeit.com/practice')

# locating open tab button using the partial link text locator
open_tab_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Tab')
open_tab_button.click()
driver.quit()
