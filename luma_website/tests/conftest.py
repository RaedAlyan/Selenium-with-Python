import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=['Chrome'], scope='class')
def setup_teardown(request):
    """
    This function is used to implement the setup and teardown stages using fixture feature.

    Returns:
        driver: a driver instance.
    """
    driver = None
    print('Setup Phase')
    if request.param == 'Chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
    elif request.param == 'Firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager("").install()))
    yield driver
    print('Teardown Phase')
    driver.quit()
