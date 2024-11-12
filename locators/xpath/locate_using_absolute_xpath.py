from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')

# Locating login button using the absolute xpath.
login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button')
login_button.click()
driver.quit()
