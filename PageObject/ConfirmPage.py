from selenium.webdriver.common.by import By


class ConfirmPage :

    def __init__(self , driver):
        self.driver = driver

    CountryFiled = (By.ID , "country")
    selectCountry = (By.XPATH, "//div[@class='suggestions']/ul[1]")
    checkbox = (By.XPATH , "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CLASS_NAME , "btn-success")
    successMessage = (By.CSS_SELECTOR , ".alert-success.alert-dismissible")

    def EnterCountryName(self):
        return self.driver.find_element(*ConfirmPage.CountryFiled)

    def SelectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def SelectCheckBox(self):
        return self.driver.find_element(*ConfirmPage.boxselect)

    def PurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def GetSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)