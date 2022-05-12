from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
url = 'http://www.seleniumframework.com/Practiceform/'
driver.get(url)
sleep(10)
driver.find_element(By.XPATH, "//a[text()='New Browser Tab']").click()
select = Select(driver.find_element(By.TAG_NAME, 'select'))
select.select_by_visible_text('New Browser Tab')
new_tab_button = element = driver.find_element(By.CSS_SELECTOR, "#newBrwTab")
new_tab_button.click()
sleep(10)
first_tab = driver.window_handles[0]
second_tab = driver.window_handles[1]

driver.switch_to.window(second_tab)
driver.close(second_tab)
sleep(5)
driver.switch_to.window(first_tab)
driver.close(first_tab)