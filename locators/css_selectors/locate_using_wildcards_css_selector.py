from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://the-internet.herokuapp.com/checkboxes')

# Approach #1: using ^ wildcard

# to locate elements that have an attribute value which starts with a check value.
checkbox_elements = driver.find_elements(By.CSS_SELECTOR, 'input[type^="check"]')
print(f'We have {len(checkbox_elements)} checkboxes which have the type attribute that start with "check" value')

# Approach #2: using the $ wildcard
# to locate elements that have an attribute value which ends with a box value.
checkbox_elements = driver.find_elements(By.CSS_SELECTOR, 'input[type$="box"]')
print(f'We have {len(checkbox_elements)} checkboxes which have the type attribute that end with "box" value')

# Approach #3: using the * wildcard

# to locate elements that have an attribute value which contains an ox substring value.
checkbox_elements = driver.find_elements(By.CSS_SELECTOR, 'input[type*="ox"]')
print(f'We have {len(checkbox_elements)} checkboxes which have the type attribute that contains "ox" substring value')

# Approach #4: using the ~ wildcard

# to locate elements that have an attribute value which contains a specific checkbox value.
checkbox_elements = driver.find_elements(By.CSS_SELECTOR, 'input[type~="checkbox"]')
print(f'We have {len(checkbox_elements)} checkboxes which have the type attribute that contains a specific "checkbox" value')

driver.quit()
