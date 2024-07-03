from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.thegoldbugs.com/')
driver.maximize_window()
checkbox_element = driver.find_element(By.CLASS_NAME, 'vnLLkKq87liyzPxn4wMB')
if checkbox_element.is_selected():  # to check if the checkbox is selected or not.
    print('This checkbox is selected')
else:
    print('This checkbox is not selected')
    checkbox_element.click()  # to select this checkbox.
driver.quit()
