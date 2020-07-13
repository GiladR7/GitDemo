import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\gilad\\PycharmProjects\\Facebook Project\\chromedriver.exe")

driver.get("https://www.makemytrip.com/")
time.sleep(3)
driver.find_element_by_id("fromCity").click()
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("isr")
DropDownOne = driver.find_element_by_id("react-autowhatever-1")
cities = DropDownOne.find_elements_by_class_name("blackText")
print(len(cities))

for city in cities:

    print(city.text)
    if(city.text == "Bangalore, India"):
        city.click()
        break

