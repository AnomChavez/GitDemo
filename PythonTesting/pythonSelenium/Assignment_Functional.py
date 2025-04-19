from selenium import webdriver

import time

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []



service_obj = Service("/Users/anomchavez/Documents/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

# 5 seconds is the max time out... 2 seconds (3 seconds saved)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)




results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

#chainning of web elements, chaining the parent element to child element to construct dynamically
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


#Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)  #48 + 160 + 180

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAMT").text)

assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)


discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalAmount > discountedAmount


time.sleep(2)





