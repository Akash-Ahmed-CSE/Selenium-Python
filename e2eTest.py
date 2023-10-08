from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(r"D:\Projects\Selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Navigate to "Shop"

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()

products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        #add Item in the cart
        product.find_element(By.XPATH,"div/button").click()
        print(product.find_element(By.XPATH,"div/button").text)

time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"button[class = 'btn btn-success']").click()

time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("Ind")
time.sleep(2)
wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT,"India").click()

time.sleep(2)
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
success = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in success

#driver.get_screenshot_as_file("screen.png")
time.sleep(3)