from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time


#webdriver.Chrome(r"C:\Users\USER_NAME\Desktop\FOLDER\chromedriver")
list1 = []
list2 = []
driver = webdriver.Chrome(r"D:\Projects\Selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(By.XPATH,"(//div[@class='products'])/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons:
    list1.append(button.find_element(By.XPATH,"parent::div/parent::div/h4").text)
    button.click()
    time.sleep(1)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
time.sleep(1)

veggies = driver.find_elements(By.CSS_SELECTOR,"p.product-name")
for veg in veggies:
    list2.append(veg.text)
print(list1)
print(list2)
assert list1 == list2

driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")

driver.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()

print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)
time.sleep(2)
driver.close()