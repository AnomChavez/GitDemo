from selenium import webdriver

import time

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#google chrome options -programcreek.com
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj= Service("/Users/anomchavez/Documents/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)



driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
