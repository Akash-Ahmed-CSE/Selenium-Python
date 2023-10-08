import pytest
from selenium import webdriver
import time
@pytest.fixture()
def setup(request):
    
    driver = webdriver.Chrome(r"D:\Projects\Selenium\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    time.sleep(3)
    request.cls.driver = driver
    yield
    driver.close()
