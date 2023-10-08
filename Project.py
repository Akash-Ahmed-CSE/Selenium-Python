from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(service=Service('D:\Projects\Selenium\chromedriver.exe'))

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='name']").send_keys("asd")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='exampleCheck1']").click()
time.sleep(2)
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
time.sleep(2)
dropdown.select_by_index(1)



time.sleep(2)
driver.close()

