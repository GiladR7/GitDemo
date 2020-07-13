import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    Browser_Name =request.config.getoption("browser_name")
    if Browser_Name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\gilad\\PycharmProjects\\Facebook Project\\chromedriver.exe")


    elif Browser_Name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\gilad\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe")


    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
