import pytest
from luma_website.pages.create_account_page import CreateAccountPage
from luma_website.configurations.testData import TestData


class TestCreateAccountPage:

    def test_create_account(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(TestData.SIGN_UP_URL)
        self.driver.maximize_window()
        sign_up_obj = CreateAccountPage(self.driver)
        sign_up_obj.create_an_account()
        title = sign_up_obj.get_title(self.driver)
        assert title == 'My Account'
