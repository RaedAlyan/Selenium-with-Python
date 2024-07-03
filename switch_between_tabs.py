from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

First_URL = 'https://www.google.com/'
SECOND_URL = 'https://www.python.org/'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(First_URL)
driver.switch_to.new_window('tab')  # to open a new tab
driver.get(SECOND_URL)
handles = driver.window_handles  # to get all windows handles
for handle in handles:
    driver.switch_to.window(handle)
    print(f'Now we are in this page: {driver.title}')
driver.quit()
