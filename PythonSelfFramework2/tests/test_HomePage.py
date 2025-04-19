import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):

        log = self.getLogger()

        #driver.find(By.CSS_SELECTOR, "[name='name']").send_keys("Rahul")
        homepage = HomePage(self.driver)

        #tuple
        # homepage.getName().send_keys(getData[0])
        # homepage.getEmail().send_keys(getData[1])

        #dictionary
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])

        homepage.getCheckBox().click()
        #sel = Select(homepage.getGender())
        #sel.select_by_visible_text("Male")

        # tuple
        #self.selectOptionByText(homepage.getGender(), getData[2])

        #dictionary
        self.selectOptionByText(homepage.getGender(),getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert("Success" in alertText)
        self.driver.refresh()

    #Tuple
    # @pytest.fixture(params=[("Rahul", "Shetty", "Male"),("Anshika", "Shetty", "Female")])
    # def getData(self, request):
    #      return request.param

    #dictionary
    @pytest.fixture(params=HomePageData.test_Homepage_data)
    def getData(self, request):
        return request.param
