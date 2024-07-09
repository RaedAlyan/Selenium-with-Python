import luma_website.configurations.testData as TestData
from luma_website.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'pass')
    SIGN_IN_BUTTON = (By.XPATH, '//button[@name="send" and @id="send2"]')
    FORGET_PASSWORD_LINK = (By.XPATH, '//*[@id="login-form"]/fieldset/div[4]/div[2]/a')
    CREATE_ACCOUNT_LINK = (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[2]/div[2]/div/div/a')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.type_text_action(element=self.EMAIL_INPUT, text=TestData.email)
        self.type_text_action(element=self.PASSWORD_INPUT, text=TestData.password)
        self.click_action(element=self.SIGN_IN_BUTTON)
