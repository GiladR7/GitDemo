from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Users\\gilad\\PycharmProjects\\Facebook Project\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//a[contains(@href , 'shop')]").click()
Products = driver.find_elements_by_xpath("//div[@class='card-body']/h4")

for Product in Products:
    if Product.text == 'Blackberry':
        Product.find_element_by_xpath("parent::div/following-sibling::div/button").click()

driver.find_element_by_css_selector("a.btn-primary").click()
driver.find_element_by_css_selector("button.btn-success").click()

driver.find_element_by_id("country").send_keys("ind")
WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul[1]")))

driver.find_element_by_xpath("//div[@class='suggestions']/ul[1]").click()
Script = "return document.getElementById('country').value"
CountryName = driver.execute_script(Script)

assert "India" == CountryName
WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='checkbox checkbox-primary']"))).click()


assert driver.find_element_by_id("checkbox2").is_selected()
driver.find_element_by_class_name("btn-success").click()
Success = driver.find_element_by_css_selector(".alert-success.alert-dismissible").text.strip()
print(Success)

assert  "Success! Thank you! Your order will be delivered in next few weeks :-)." in Success
