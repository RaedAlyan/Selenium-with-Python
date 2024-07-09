import pytest
from luma_website.pages.create_account_page import CreateAccountPage
import luma_website.configurations.testData as TestData


class TestCreateAccountPage:

    def test_create_account(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(TestData.sign_up_page)
        self.driver.maximize_window()
        sign_up_obj = CreateAccountPage(self.driver)
        sign_up_obj.create_an_account()
        title = sign_up_obj.get_title(self.driver)
        assert title == 'My Account'
