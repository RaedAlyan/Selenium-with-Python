from collections import namedtuple
from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class Locators:
    Locators = namedtuple('Locators', ['locator_selector', 'element'])
    booking_form_btn = Locators(locator_selector=By.XPATH, element='//*[@id="mainNavigation"]/div[4]/a')
    first_name_input = Locators(locator_selector=By.NAME, element='fname')
    last_name_input = Locators(locator_selector=By.NAME, element='lname')
    email_input = Locators(locator_selector=By.ID, element='email-yui_3_17_2_1_1664570076619_2728-field')
    subject_input = Locators(locator_selector=By.ID, element='text-yui_3_17_2_1_1664570076619_2729-field')
    message_input = Locators(locator_selector=By.ID, element='textarea-yui_3_17_2_1_1664570076619_2730-field')
    response_required_checkbox = Locators(locator_selector=By.CLASS_NAME, element='vnLLkKq87liyzPxn4wMB')
    private_show_radio_btn = Locators(locator_selector=By.ID, element='yui_3_17_2_1_1716542294533_552')
    select_dropdown = Locators(locator_selector=By.ID, element='select-e1f50715-c8a7-48eb-bc99-2c245676068c-field')
    survey_radio_btn = Locators(locator_selector=By.CLASS_NAME, element='BBtGxw_hkkxfQT5_KoPf')
    submit_btn = Locators(locator_selector=By.XPATH, element='//*[@id="yui_3_17_2_1_1714737908343_497"]/div[3]/button')
