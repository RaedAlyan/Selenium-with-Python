from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.thegoldbugs.com/')
driver.set_page_load_timeout(10)
radio_button_element = driver.find_element(By.CLASS_NAME, 'loj47NF2EW4uatXeLLmw')
radio_button_element.click()
if radio_button_element.is_selected():
    print('This radio button is selected')
else:
    print('This radio button is not selected.')
    radio_button_element.click()
driver.quit()
