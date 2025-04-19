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

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID, "tinymce").click()

driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)

time.sleep(2)

# can do further practice on frames on rahulshetty.com/AutomationPractice page