from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver
# service_obj= Service("/Users/anomchavez/Documents/chromedriver-mac-arm64/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

#Firefox
# service_obj= Service("/Users/anomchavez/Documents/geckodriver")
# driver = webdriver.Firefox(service=service_obj)

#Edge
service_obj= Service("/Users/anomchavez/Documents/edgedriver_mac64_m1/msedgedriver")
driver = webdriver.Edge(service=service_obj)


driver.maximize_window()
driver.get("https://rahulshettyacademy.com")

print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/practice-project")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()