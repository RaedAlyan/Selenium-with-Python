from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.google.com/')
driver.maximize_window()
search_input = WebDriverWait(driver, 30).until(
    ec.visibility_of_element_located((By.XPATH, '//*[@id="APjFqb"]'))
)

actions = ActionChains(driver)  # Initialize ActionChains
actions.click(search_input).send_keys('Python').send_keys(Keys.ENTER).perform()  # send Python and click Enter.
driver.quit()
