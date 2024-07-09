import time
import luma_website.configurations.testData as TestData
from luma_website.pages.login_page import LoginPage


class TestLoginPage:

    def test_login(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(TestData.sign_in_page)
        self.driver.maximize_window()
        sign_in_obj = LoginPage(self.driver)
        sign_in_obj.login()
        time.sleep(2)
        title = sign_in_obj.get_title(self.driver)
        assert title == 'My Account',  "Login Not Successful"

    def test_login_page_title(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(TestData.sign_in_page)
        self.driver.maximize_window()
        sign_in_obj = LoginPage(self.driver)
        time.sleep(2)
        title = sign_in_obj.get_title(self.driver)
        assert title == 'Customer Login',  "Not a valid Page"
