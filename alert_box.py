from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
url = 'http://www.seleniumframework.com/Practiceform/'
driver.get(url)
sleep(5)

driver.find_element(By.CSS_SELECTOR, "#alert").click()
alert = browser.switch_to.alert
alert.accept()