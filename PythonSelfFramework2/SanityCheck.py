#just checking that the environment is working as expected
#change from Alt user

from selenium import webdriver

import time

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj= Service("/Users/anomchavez/Documents/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#   a[href*='shop'] CSS  //a[contains(@href,'shop')] XPATH partial value references using href using regular expressions

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

browserSortedCards = []

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")


for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
time.sleep(2)

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successText

driver.close()











