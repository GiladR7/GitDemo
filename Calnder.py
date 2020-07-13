from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\gilad\\PycharmProjects\\Facebook Project\\chromedriver.exe")

driver.get("https://www.trip.com/")
driver.find_element_by_xpath("//*[@class='calendar-container']/div[1]").click()
month = driver.find_element_by_css_selector("[class='c-calendar__body'] div:nth-child(1) h3").text




while("Sep" not in month):
    driver.find_element_by_class_name("c-calendar-icon-next").click()
    month = driver.find_element_by_css_selector("[class='c-calendar__body'] div:nth-child(1) h3").text


days = driver.find_elements_by_class_name("is-allow-hover")

for day in days:
    IndexsOfDay = days.index(day)
    if day.text == "3":
        day.click()
    elif day.text == "23":
        day.click()
        break

while(rooms != 3):
    driver.find_element_by_xpath("//*[@class='choice']/div[1]/div/span[3]").click()
    rooms = driver.find_element_by_xpath("//*[@class='choice']/div[1]/div/span[2]").text





