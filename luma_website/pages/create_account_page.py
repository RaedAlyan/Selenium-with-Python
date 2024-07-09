from selenium.webdriver.common.by import By
from luma_website.pages.base_page import BasePage
import luma_website.configurations.testData as TestData


class CreateAccountPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'firstname')
    LAST_NAME_INPUT = (By.ID, 'lastname')
    EMAIL_INPUT = (By.ID, 'email_address')
    PASSWORD_INPUT = (By.ID, 'password')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'password-confirmation')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')

    def __init__(self, driver):
        super().__init__(driver)

    def create_an_account(self):
        """
        This method is used to automate creating an account process.

        """
        self.type_text_action(element=self.FIRST_NAME_INPUT, text=TestData.first_name)
        self.type_text_action(element=self.LAST_NAME_INPUT, text=TestData.last_name)
        self.type_text_action(element=self.EMAIL_INPUT, text=TestData.email)
        self.type_text_action(element=self.PASSWORD_INPUT, text=TestData.password)
        self.type_text_action(element=self.CONFIRM_PASSWORD_INPUT, text=TestData.password)
        self.click_action(element=self.CREATE_ACCOUNT_BUTTON)