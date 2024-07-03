from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://magento.softwaretestingboard.com/customer/account/login')
email_input = driver.find_element(By.XPATH, '//input[@id="email" and @title="Email"]')
email_input.send_keys('raed@gmail.com')
password_input = driver.find_element(By.XPATH, '//input[@id="pass" and @title="Password"]')
password_input.send_keys('123@!')
singin_button = driver.find_element(By.XPATH, '//button[@id="send2" and @name="send"]')
singin_button.click()
driver.quit()