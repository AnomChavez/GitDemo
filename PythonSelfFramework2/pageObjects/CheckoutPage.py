from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    #driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    #driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    #driver.find_element(By.ID, "country").send_keys("ind")
    #driver.find_element(By.LINK_TEXT, "India").click()

    #productName = product.find_element(By.XPATH, "div/h4/a").text
    product = (By.XPATH, "//div[@class='card h-100']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")
    primaryButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    countryField = (By.ID, "country")
    IndiaText = (By.LINK_TEXT, "India")


    def getproduct(self):
        return self.driver.find_elements(*CheckOutPage.product)

    def getcheckOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def getprimaryButton(self):
        return self.driver.find_element(*CheckOutPage.primaryButton)

    def getcountryField(self):
        return self.driver.find_element(*CheckOutPage.countryField)

    def getIndiaText(self):
        return self.driver.find_element(*CheckOutPage.IndiaText)


    def selectProductByName(self, name):
        products = self.getproduct()  # reuse the method you already have
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == name:
                product.find_element(By.XPATH, "div/button").click()
                break





