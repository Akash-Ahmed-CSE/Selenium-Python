from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(service=Service('D:\Projects\Selenium\chromedriver.exe'))

driver.get("https://www.makemytrip.com/")
time.sleep(3)
driver.maximize_window()
driver.find_element(By.ID, "fromCity").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='From']").send_keys("del")
time.sleep(2)
cities_From = driver.find_elements(By.CSS_SELECTOR,"p[class*='blackText']")
time.sleep(2)

#From City
city_From = None
for city_From in cities_From:
    if city_From.text == "Cali, Colombia":
        desired_suggestion = city_From
        break
print(desired_suggestion)
if desired_suggestion is not None:
    desired_suggestion.click()

time.sleep(2)
#To City
driver.find_element(By.ID, "toCity").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='To']").send_keys("New")
cities_To = driver.find_elements(By.CSS_SELECTOR,"p[class*='blackText']")
city_To = None
desired_suggestion_To = None
for city_To in cities_To:
    if city_To.text == "New Delhi, India":
        desired_suggestion_To = city_To
        break
print(desired_suggestion_To)
time.sleep(5)
if desired_suggestion_To is not None:
    desired_suggestion_To.click()

time.sleep(5)
driver.close()