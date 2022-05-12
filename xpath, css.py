from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.maximize_window()

url = 'http://automationpractice.com/index.php'

driver.get(url)

try:
     element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='Contact us']"))
    )
except TimeoutException:
    print('Waited for 10 sec, could not locate the element')
else: 
    element.click()        

select = Select(driver.find_element(By.CSS_SELECTOR, '#id_contact'))
select.select_by_index(1)
email = driver.find_element(By.CSS_SELECTOR, '#email')
element = driver.find_element(By.CSS_SELECTOR, "#email")
order = driver.find_element(By.CSS_SELECTOR, "#order")
element = driver.find_element(By.CSS_SELECTOR, "#id_order")
driver.find_element(By.XPATH, "//a[text()='Attach File']").click()
choose_file = driver.find_element(By.CSS_SELECTOR, "#fileUpload").send_keys(r'C:\AUTOMATION\Ebanq\1.txt')
file_path = r'C:\AUTOMATION\Ebanq\1.txt'
choose_file.send_keys(file_path)
driver.find_element(By.CSS_SELECTOR, "#message").send_keys('test')
driver.find_element(By.XPATH, "//button[@name='submitMessage']").click()



#select.select_by_visible_text('Customer service')
#select = Select(driver.find_element(By.TAG_NAME, 'Subject Heading'))
# driver.find_element(By.XPATH, "//a[text()='Customer service']").submit()
#driver.find_element(By.XPATH, "//a[text()='Contact us']").click()