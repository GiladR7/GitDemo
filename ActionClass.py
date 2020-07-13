from selenium.webdriver import ActionChains

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\gilad\\PycharmProjects\\Facebook Project\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()
driver.switch_to.alert.accept()


