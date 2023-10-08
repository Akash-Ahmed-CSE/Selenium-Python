from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(r"D:\Projects\Selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#DOM
driver.find_element(By.XPATH,"//input[@id='displayed-text']").send_keys("Hello")
time.sleep(3)
print(driver.find_element(By.XPATH,"//input[@id='displayed-text']").get_attribute("value"))
time.sleep(3)