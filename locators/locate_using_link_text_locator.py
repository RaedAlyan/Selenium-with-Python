from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.letskodeit.com/practice')

# locating open tab button using the link text locator
open_tab_button = driver.find_element(By.LINK_TEXT, 'Open Tab')
open_tab_button.click()
driver.quit()
