import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://books.toscrape.com/')
driver.execute_script("confirm('Hey! Do you want to confirm?')")  # to create an alert using JS.
time.sleep(5)
alert = driver.switch_to.alert  # to switch to the current alert in the webpage.
print(alert.text)  # print the alert text
alert.accept()  # to accept the alert.
# alert.dismiss()  # to dismiss the alert.
time.sleep(5)
driver.quit()

