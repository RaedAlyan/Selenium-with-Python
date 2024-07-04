import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.implicitly_wait(time_to_wait=30)  # implicit wait.
driver.maximize_window()
driver.get('https://magento.softwaretestingboard.com/customer/account/login')
time.sleep(15)  # unconditional synchronization (static wait)
driver.find_element(By.XPATH, "//*[@id='email' and @type='email']").send_keys("raed@gmail.com")
driver.find_element(By.XPATH, "//input[@id='pass' or @title='password']").send_keys("raed123@")
driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
driver.find_element(By.XPATH, "//*[contains(text(),'Subs')]").click()
driver.quit()
