import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from main_page import BookingForm


class TestFillForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get('https://www.thegoldbugs.com/')
        cls.page = BookingForm(cls.driver)
        # cls.page.click_booking_form_button()

    def setUp(self):
        pass

    def test_fill_form(self):
        self.page.fill_form(first_name='Raed', last_name='Eleyan', email='raed@gmail.com', subject='Test Subject',
                            message='Test Message', option='Facebook')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
