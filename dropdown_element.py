from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.thegoldbugs.com/')
dropdown_element = driver.find_element(By.ID, 'select-e1f50715-c8a7-48eb-bc99-2c245676068c-field')
dropdown = Select(dropdown_element)
dropdown.select_by_index(1)
dropdown.select_by_value('Google')
dropdown.select_by_visible_text('Facebook')
driver.quit()


