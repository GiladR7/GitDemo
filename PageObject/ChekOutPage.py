from selenium.webdriver.common.by import By

from PageObject.ConfirmPage import ConfirmPage


class ChekOutPage:

    def __init__(self, driver):
        self.driver = driver

    Products = (By.XPATH, "//div[@class='card-body']/h4")
    AddCart = (By.CSS_SELECTOR, "button.btn-info")
    ForwardToChekOutPage = (By.CSS_SELECTOR, "a.btn-primary")
    OverChekOut = (By.CSS_SELECTOR, "button.btn-success")

    def ProductsName(self):
        return self.driver.find_elements(*ChekOutPage.Products)

    def AddToCart(self):
        return self.driver.find_elements(*ChekOutPage.AddCart)

    def ForwardToChekOut(self):
        return self.driver.find_element(*ChekOutPage.ForwardToChekOutPage)

    def ClickOnCheckOut(self):
         self.driver.find_element(*ChekOutPage.OverChekOut).click()
         confirm = ConfirmPage(self.driver)
         return confirm
