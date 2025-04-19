import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
#@pytest.mark.usefixtures("setup")
from utilities.BaseClass import BaseClass



class TestOne(BaseClass):
    driver: WebDriver # <-- This tells PyCharm what `self.driver` is

    def test_e2e(self):
        log = self.getLogger()

        log.info("Navigating to home page")
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        log.info("Clicked on Shop menu")
        checkOutPage = CheckOutPage(self.driver)
        log.info("Selected Blackberry")
        confirmPage = ConfirmPage(self.driver)
        products = checkOutPage.getproduct()

        checkOutPage.selectProductByName("Blackberry")
        checkOutPage.getprimaryButton().click()
        checkOutPage.getcheckOutItems().click()
        checkOutPage.getcountryField().send_keys("ind")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        checkOutPage.getIndiaText().click()
        confirmPage.getcheckBox().click()
        confirmPage.getsubmitButton().click()
        successText = confirmPage.getsuccessAlert().text
        assert "Success! Thank you!" in successText
        #self.driver.close()


