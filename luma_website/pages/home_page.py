from luma_website.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    WOMEN_PAGE_LINK = (By.XPATH, '//*[@id="ui-id-4"]')
    MEN_PAGE_LINK = (By.XPATH, '//*[@id="ui-id-5"]')

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_women_page(self):
        self.click_action(element=self.WOMEN_PAGE_LINK)

    def go_to_men_page(self):
        self.click_action(element=self.MEN_PAGE_LINK)
