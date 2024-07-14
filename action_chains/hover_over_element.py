from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.python.org/')
driver.maximize_window()
download_link = WebDriverWait(driver, 30).until(
    ec.element_to_be_clickable((By.XPATH, '//*[@id="downloads"]/a'))
)

actions = ActionChains(driver)  # Initialize ActionChains
actions.move_to_element(download_link).perform()  # Hover over the element
driver.quit()
