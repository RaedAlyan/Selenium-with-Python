"""
    --> Project Name: Python version Scraper.
    --> Goal: Scrape the latest python release version from the official website.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.google.com')
driver.maximize_window()
try:
    search_area = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'APjFqb'))
    )
    search_area.send_keys('python')
    search_area.submit()
    python_download_page = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//a[@href="https://www.python.org/downloads/"]'))
    )
    python_download_page.click()
    python_download_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Download Python'))
    )
    latest_release_version = ' '.join(python_download_btn.text.split()[1:])
    print(f'The latest Python release version is: {latest_release_version}')
except NoSuchElementException as e:
    print('No elements meet the criteria in the desired web page.', e)
finally:
    driver.quit()
