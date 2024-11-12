from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.letskodeit.com/practice')

# locating using the text()
open_window_button = driver.find_element(By.XPATH, '//button[text()="Open Window"]')
open_window_button.click()

# locating using the contains()
open_window_button = driver.find_element(By.XPATH, '//button[contains(text(),"Window")]')
open_window_button.click()

# locating using the starts-with()
open_tap_button = driver.find_element(By.XPATH, '//a[starts-with(@id, "open")]')
open_tap_button.click()

driver.quit()

