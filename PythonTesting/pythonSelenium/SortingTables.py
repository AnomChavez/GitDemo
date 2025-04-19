from selenium import webdriver

import time

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browserSortedVeggies = []

service_obj= Service("/Users/anomchavez/Documents/geckodriver")
driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(2)

#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#collect all veggie names -> BrowserSortedveggieList (A,B,C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

#Sort this browserSortedVeggiesList => new SortedList -> (A,B,C)
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList

print(browserSortedVeggies)
print(originalBrowserSortedList)
# veggieList == newSortedList




