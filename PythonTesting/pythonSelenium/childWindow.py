from selenium import webdriver

import time

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("/Users/anomchavez/Documents/geckodriver")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, 'Click Here').click()
windowsOpened = driver.window_handles

print(driver.find_element(By.TAG_NAME, "h3").text)


driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)
driver.close()
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)
