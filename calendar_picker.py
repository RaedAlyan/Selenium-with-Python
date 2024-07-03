import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://jqueryui.com/datepicker/')
iframe_element = driver.find_element(By.CSS_SELECTOR, 'iframe.demo-frame')
driver.switch_to.frame(iframe_element)
input_element = driver.find_element(By.ID, 'datepicker')
input_element.click()  # to activate the calendar.
now = datetime.now()
year = now.year
month = now.month
day = now.day
DATE_PATH = f'//td[@data-month="{month - 1}" and @data-year="{year}"]/a[@data-date="{day}"]'
date_element = driver.find_element(By.XPATH, DATE_PATH)
date_element.click()
time.sleep(10)
driver.quit()



