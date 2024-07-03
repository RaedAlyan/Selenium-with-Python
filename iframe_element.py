from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://jqueryui.com/draggable/')
iframe_element = driver.find_element(By.TAG_NAME, 'iframe')  # find iframe element.
driver.switch_to.frame(iframe_element)  # switch to the iframe.
draggable_element = driver.find_element(By.ID, 'draggable')  # get an element inside the iframe.
driver.switch_to.default_content()  # go back to the main HTML.
sidebar_element = driver.find_element(By.ID, 'sidebar')  # to find an element in the main HTML.
driver.quit()







