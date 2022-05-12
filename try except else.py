from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

url = 'http://automationpractice.com/index.php'

driver.get(url)

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='Contacct us']"))
    )
except TimeoutException:
    print('Waited for 15 sec, could not locate the element')
else: 
    element.click()






#driver.find_element(By.XPATH, "/ /a[text()='Contact us']").click() #mistake
