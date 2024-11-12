from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.letskodeit.com/practice')

# locating using the "ancestor" axes
table_elements = driver.find_elements(By.XPATH, '//tbody/ancestor::table')
print(f'Table elements: {len(table_elements)}')

# locating using the "child" axes
direct_table_rows = driver.find_elements(By.XPATH, '//tbody/child::tr')
print(f'Table rows: {len(direct_table_rows)}')

# locating using the "descendant" axes
indirect_table_rows = driver.find_elements(By.XPATH, '//table/descendant::tr')
print(f'Table rows: {len(indirect_table_rows)}')

# locating using the "following" axes
following_table_rows = driver.find_elements(By.XPATH, '//tr/following::tr')
print(f'Following table rows: {len(following_table_rows)}')

# locating using the "following-sibling" axes
following_table_rows = driver.find_elements(By.XPATH, '//tr/following-sibling::tr')
print(f'Following table rows: {len(following_table_rows)}')

# locating using the "parent" axes
parent_table = driver.find_elements(By.XPATH, '//tbody/parent::table')
print(f'Parent table: {len(parent_table)}')

# locating using the "preceding" axes
preceding_table_rows = driver.find_elements(By.XPATH, '//tbody/child::tr[3]/preceding::tr')
print(f'Preceding table rows: {len(preceding_table_rows)}')

# locating using the "preceding-sibling" axes
preceding_sibling_table_rows = driver.find_elements(By.XPATH, '//tbody/child::tr[3]/preceding-sibling::tr')
print(f'Preceding sibling table rows: {len(preceding_sibling_table_rows)}')
driver.quit()
