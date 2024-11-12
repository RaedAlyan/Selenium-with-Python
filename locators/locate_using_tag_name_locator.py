from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.letskodeit.com/practice')

# locating all <a> tags using the tag name locator
a_tags = driver.find_elements(By.TAG_NAME, 'a')
print(f'Number of tags: {len(a_tags)}')
driver.quit()
