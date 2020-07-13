from selenium.webdriver.common.by import By

from PageObject.ChekOutPage import ChekOutPage


class Home_Page:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH , "//a[contains(@href , 'shop')]")
    nameField = (By.CSS_SELECTOR , "[class='form-group'] [name='name']")
    emailField = (By.XPATH , "//*[@name='email']")
    passwordField = (By.CSS_SELECTOR , "[type='password']")
    CheckBox = (By.ID ,"exampleCheck1")
    submit = (By.CSS_SELECTOR ,"[type='submit']")
    dropdown = (By.ID , "exampleFormControlSelect1")
    success = (By.CSS_SELECTOR , ".alert-success")


    def shopitems(self):
         self.driver.find_element(*Home_Page.shop).click()
         checkout = ChekOutPage(self.driver)
         return checkout

    def EnterName(self):
        return self.driver.find_element(*Home_Page.nameField)

    def EnterEmail(self):
        return self.driver.find_element(*Home_Page.emailField)

    def EnterPassword(self):
        return self.driver.find_element(*Home_Page.passwordField)

    def SelectCheckBox(self):
        return self.driver.find_element(*Home_Page.CheckBox)

    def getGender(self):
        return self.driver.find_element(*Home_Page.dropdown)

    def Submut(self):
        return self.driver.find_element(*Home_Page.submit)

    def getMessage(self):
        return self.driver.find_element(*Home_Page.success)


