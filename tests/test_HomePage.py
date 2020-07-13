import time
import pytest
from Data.Home_Page_Data import HomePage_date
from PageObject.HomePage import Home_Page
from utilities.BassClass import BaseClass


class Test_Home_Page(BaseClass):

    def test_home_page(self , getDate):
        home_page = Home_Page(self.driver)
        home_page.EnterName().send_keys(getDate["firstname"])
        home_page.EnterEmail().send_keys(getDate["email"])
        home_page.EnterPassword().send_keys(getDate["password"])
        home_page.SelectCheckBox().click()
        self.SelectDropDown(home_page.getGender(),getDate["gender"])
        home_page.Submut().click()

        assert "Success" in home_page.getMessage().text
        time.sleep(3)
        self.driver.refresh()

    @pytest.fixture(params= HomePage_date.home_page_data)
    def getDate(self ,request):
        return request.param
