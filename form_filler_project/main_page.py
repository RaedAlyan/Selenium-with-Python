from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_page_locators import Locators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, selector, element):
        web_element = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((selector, element))
        )
        return web_element

    def enter_text(self, selector, element, text):
        web_element = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((selector, element))
        )
        web_element.send_keys(text)

    def click(self, selector, element):
        web_element = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((selector, element))
        )
        web_element.click()
        return web_element


class BookingForm(MainPage):

    def click_booking_form_button(self):
        booking_form_btn = WebDriverWait(self.driver, 300).until(
            EC.element_to_be_clickable((Locators.booking_form_btn.locator_selector,
                                        Locators.booking_form_btn.element))
        )
        booking_form_btn.click()

    def fill_first_name(self, first_name):
        self.enter_text(Locators.first_name_input.locator_selector, Locators.first_name_input.element, first_name)

    def fill_last_name(self, last_name):
        self.enter_text(Locators.last_name_input.locator_selector, Locators.last_name_input.element, last_name)

    def fill_email(self, email):
        self.enter_text(Locators.email_input.locator_selector, Locators.email_input.element, email)

    def fill_subject(self, subject):
        self.enter_text(Locators.subject_input.locator_selector, Locators.subject_input.element, subject)

    def fill_message(self, message):
        self.enter_text(Locators.message_input.locator_selector, Locators.message_input.element, message)

    def choose_option(self):
        element = self.click(Locators.response_required_checkbox.locator_selector,
                             Locators.response_required_checkbox.element)
        if not element.is_selected():
            raise ElementNotSelectableException('The option is not selected')

    def select_type_event(self):
        element = self.click(Locators.private_show_radio_btn.locator_selector, Locators.private_show_radio_btn.element)
        if not element.is_selected():
            raise ElementNotSelectableException('The type event radio button is not selected.')

    def select_drop_down(self, option):
        select_element = self.get_element(Locators.select_dropdown.locator_selector, Locators.select_dropdown.element)
        select = Select(select_element)
        select.select_by_value(option)

    def click_survey_btn(self):
        survey_btn = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((Locators.survey_radio_btn.locator_selector, Locators.survey_radio_btn.element))
        )
        survey_btn.click()

    def submit_form(self):
        submit_btn = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((Locators.submit_btn.locator_selector, Locators.submit_btn.element))
        )
        submit_btn.click()

    def fill_form(self, first_name, last_name, email, subject, message, option):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_subject(subject)
        self.fill_message(message)
        self.choose_option()
        self.select_type_event()
        self.select_drop_down(option)
        self.click_survey_btn()
        self.submit_form()
