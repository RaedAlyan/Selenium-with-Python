from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def type_text_action(self, element, text):
        WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(element)
        ).send_keys(f'{text}')

    def click_action(self, element):
        WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable(element)
        ).click()

    def get_text_element(self, element):
        text_element = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(element)
        ).text
        return text_element
    
    @staticmethod
    def get_title(driver):
        return driver.title


