import luma_website.configurations.testData as TestData
from luma_website.pages.home_page import HomePage


class TestHomePage:

    def test_navigate_to_men_page(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(TestData.home_page)
        self.driver.maximize_window()
        home_page_obj = HomePage(self.driver)
        home_page_obj.go_to_men_page()
        title = home_page_obj.get_title(self.driver)
        assert title == 'Men', 'Invalid Page'

    def test_navigate_to_women_page(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(TestData.home_page)
        self.driver.maximize_window()
        home_page_obj = HomePage(self.driver)
        home_page_obj.go_to_women_page()
        title = home_page_obj.get_title(self.driver)
        assert title == 'Women', 'Invalid Page'
