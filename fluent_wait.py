from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.maximize_window()
driver.get('https://magento.softwaretestingboard.com/customer/account/login')
wait = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[NoSuchElementException])  # fluent wait.
wait.until(
    ec.visibility_of_element_located((By.XPATH, "//*[@id='email' and @type='email']"))
).send_keys('raed@gmail.com')

wait.until(
    ec.visibility_of_element_located((By.XPATH, "//input[@id='pass' or @title='password']"))
).send_keys('raed123@')

wait.until(
    ec.element_to_be_clickable((By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]"))
).click()

driver.quit()