from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.letskodeit.com/practice')


# locating open window button using ID locator
open_window_button = driver.find_element(By.ID, 'openwindow')
open_window_button.click()
driver.quit()
