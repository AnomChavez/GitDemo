from selenium import webdriver

import time

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj= Service("/Users/anomchavez/Documents/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scroll(0,document.body.scrollHeight);")
time.sleep(3)
driver.get_screenshot_as_file("screen.png")