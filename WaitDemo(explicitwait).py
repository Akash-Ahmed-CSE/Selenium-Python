from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome(service=Service('D:\Projects\Selenium\chromedriver.exe'))


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(By.XPATH,"(//div[@class='products'])/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
for button in buttons:
    button.click()
    time.sleep(1)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,"input[placeholder='Enter promo code']"))
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")

driver.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()
wait.until(expected_conditions.presence_of_element_located(By.XPATH,"//span[@class='promoInfo']"))
print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)
time.sleep(2)
driver.close()