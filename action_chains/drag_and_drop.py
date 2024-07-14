from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://jqueryui.com/droppable/')
driver.maximize_window()
iframe_element = driver.find_element(By.CSS_SELECTOR, 'iframe.demo-frame')
driver.switch_to.frame(iframe_element)
source_element = WebDriverWait(driver, 30).until(
    ec.visibility_of_element_located((By.ID, 'draggable'))
)

target_element = WebDriverWait(driver, 30).until(
    ec.visibility_of_element_located((By.ID, 'droppable'))
)

actions = ActionChains(driver)  # Initialize ActionChains
actions.drag_and_drop(source=source_element, target=target_element).perform()  # perform drag and drop
driver.switch_to.default_content()
driver.quit()
