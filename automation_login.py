"""
    We want to automate the following steps:
        1- Open a web browser (Chrome).
        2- Open a URL: https://www.saucedemo.com/
        3- Provide an email: standard_user.
        4- Provide a password: secret_sauce.
        5- Click on the login button.
        6- Verify the title.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.refresh()
driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print(driver.title)
driver.close()
driver.quit()
