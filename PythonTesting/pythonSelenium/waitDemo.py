from selenium import webdriver

import time

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("/Users/anomchavez/Documents/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

# 5 seconds is the max time out... 2 seconds (3 seconds saved)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

#chainning of web elements, chaining the parent element to child element to construct dynamically
for result in results:
    result.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
time.sleep(2)





