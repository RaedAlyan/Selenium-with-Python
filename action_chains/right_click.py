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
about_link = WebDriverWait(driver, 30).until(
    ec.presence_of_element_located((By.XPATH, '//*[@id="about"]/a'))
)

actions = ActionChains(driver)  # Initialize ActionChains
actions.context_click(about_link).perform()  # perform right click (context click).
driver.quit()
