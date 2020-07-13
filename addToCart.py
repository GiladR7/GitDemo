from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Users\\gilad\\PycharmProjects\\Facebook Project\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
ListOfProducts = ["Cauliflower", "Beans", "Potato" ,"Brinjal" ,"Capsicum"]
products = driver.find_elements_by_xpath("//*[@class='product']/h4")
AddToCart = driver.find_elements_by_xpath("//*[text()='ADD TO CART']")
AddProduct = 0
Sum = 0
try :
    for product in products:
        productName = product.text.split()
        productIndex = products.index(product)
        if productName[0].strip() in ListOfProducts:
            AddToCart[productIndex].click()
            AddProduct+=1

        if AddProduct == len(ListOfProducts):
            print(AddProduct)
            break

    driver.find_element_by_css_selector(".cart-icon").click()
    driver.find_element_by_xpath("//*[@class='action-block']/button").click()
    WebDriverWait(driver , 3).until(EC.presence_of_element_located((By.XPATH , "//*[@class='promoCode']")))
    amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
    for amount in amounts:
        Sum+=int(amount.text)
    print(Sum)

    Total = int(driver.find_element_by_css_selector(".totAmt").text)

    assert Sum == Total
    driver.find_element_by_xpath("//*[@class='promoCode']").send_keys("rahulshettyacademy")
    
    driver.find_element_by_class_name("promoBtn").click()

    WebDriverWait(driver , 6).until(EC.presence_of_element_located((By.CLASS_NAME , "promoInfo")))
    print(driver.find_element_by_xpath("//*[@class='promoInfo']").text)
    Discount = driver.find_element_by_css_selector(".discountPerc").text
    NumOfDiscount =Discount.split("%")
    print(NumOfDiscount)
    FinalDiscont = int(NumOfDiscount[0])
    print(FinalDiscont)
    print(Total/FinalDiscont)



finally:
    driver.close()











