import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def WaitToLink(self, text):
        WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectDropDown(self, locator, text):
        s = Select(locator)
        s.select_by_visible_text(text)
