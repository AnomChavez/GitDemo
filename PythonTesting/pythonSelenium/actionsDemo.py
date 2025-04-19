from selenium import webdriver

import time

from selenium.webdriver import ActionChains
#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
name = "Rahul"
service_obj= Service("/Users/anomchavez/Documents/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)

#action.double_click(driver.find_element(By.))
#action.context_click()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
#time.sleep(3)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(5)