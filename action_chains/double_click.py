from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demos.telerik.com/kendo-ui/treeview/animation')
driver.maximize_window()
furniture_option = WebDriverWait(driver, 30).until(
    ec.presence_of_element_located((By.XPATH, '//*[@id="treeview_tv_active"]/div/span[2]'))
)

actions = ActionChains(driver)  # Initialize ActionChains
actions.double_click(furniture_option).perform()  # perform double click.
driver.quit()
