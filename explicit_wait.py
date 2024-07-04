from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.maximize_window()
driver.get('https://magento.softwaretestingboard.com/customer/account/login')

WebDriverWait(driver, 15).until(
    ec.visibility_of_element_located((By.XPATH, "//*[@id='email' and @type='email']"))
).send_keys('raed@gmail.com')

WebDriverWait(driver, 15).until(
    ec.visibility_of_element_located((By.XPATH, "//input[@id='pass' or @title='password']"))
).send_keys('raed123@')

WebDriverWait(driver, 15).until(
    ec.element_to_be_clickable((By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]"))
).click()

driver.quit()