from luma_website.pages.home_page import HomePage
from luma_website.pages.men_page import MenPage
import luma_website.configurations.testData as TestData


class TestEndToEnd:

    def test_add_product_to_cart_and_checkout(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(TestData.home_page)
        self.driver.maximize_window()
        home_page_obj = HomePage(self.driver)
        home_page_obj.go_to_men_page()
        men_page_obj = MenPage(self.driver)
        men_page_obj.add_first_men_pants_to_chart_checkout()
        title = men_page_obj.get_title()
        print(title)
