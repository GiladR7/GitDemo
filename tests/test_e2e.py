
from PageObject.HomePage import Home_Page
from utilities.BassClass import BaseClass


class Test_One(BaseClass):

    def test_e2e(self):
        homepage = Home_Page(self.driver)
        check_out = homepage.shopitems()
        Products = check_out.ProductsName()

        i = -1
        for Product in Products:
            i+=1
            if Product.text == 'Blackberry':
                check_out.AddToCart()[i].click()

        check_out.ForwardToChekOut().click()
        confirmPage= check_out.ClickOnCheckOut()

        confirmPage.EnterCountryName().send_keys("ind")
        self.WaitToLink("India")
        confirmPage.SelectCountry().click()
        Script = "return document.getElementById('country').value"
        CountryName = self.driver.execute_script(Script)

        assert "India" == CountryName

        confirmPage.PurchaseButton().click()
        Success = confirmPage.GetSuccessMessage().text
        print(Success)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in Success