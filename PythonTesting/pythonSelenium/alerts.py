from selenium import webdriver

import time

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name = "Rahul"
service_obj= Service("/Users/anomchavez/Documents/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
time.sleep(2)
alert.accept()
#alert.dismiss()