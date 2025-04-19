from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        # successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text


    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, "[type='submit']")
    successAlert = (By.CLASS_NAME, "alert-success")


    def getcheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getsubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getsuccessAlert(self):
        return self.driver.find_element(*ConfirmPage.successAlert)



