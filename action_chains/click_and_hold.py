from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()
source_element = WebDriverWait(driver, 30).until(
    ec.presence_of_element_located((By.XPATH, '//*[@id="box7"]'))
)

target_element = WebDriverWait(driver, 30).until(
    ec.presence_of_element_located((By.XPATH, '//*[@id="box107"]'))
)

actions = ActionChains(driver)  # Initialize ActionChains
actions.click_and_hold(source_element).move_to_element(target_element).release().perform()  # perform click and hold.
driver.quit()
