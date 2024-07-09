from luma_website.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MenPage(BasePage):
    MEN_PANTS_CATEGORY_LINK = (By.XPATH, "//a[text()='Pants']")
    MEN_PANTS_FIRST_PRODUCT_LOCATION = (By.XPATH, "//div[@class='product-item-info']/parent::li/parent::ol/li[1]")
    MEN_PANTS_SIZE = (By.XPATH, "//span[text()='Size']/following-sibling::div/div[1]")
    MEN_PANTS_COLOR = (By.XPATH, "//span[text()='Color']/following-sibling::div / div[1]")
    ADD_TO_CART_BUTTON = (By.ID, "product-addtocart-button")
    CART_ICON = (By.XPATH, "/div[@data-block='minicart']")
    CHECKOUT_PROCEED = (By.ID, "top-cart-btn-checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def click_men_pants_category(self):
        self.click_action(element=self.MEN_PANTS_CATEGORY_LINK)

    def add_first_men_pants_to_chart_checkout(self):
        self.click_action(element=self.MEN_PANTS_CATEGORY_LINK)
        self.click_action(element=self.MEN_PANTS_FIRST_PRODUCT_LOCATION)
        self.click_action(element=self.MEN_PANTS_SIZE)
        self.click_action(element=self.MEN_PANTS_COLOR)
        self.click_action(element=self.ADD_TO_CART_BUTTON)
        self.click_action(element=self.CART_ICON)
        self.click_action(element=self.CHECKOUT_PROCEED)
