from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
import time


#driver = webdriver.Chrome(r"C:\Users\USER_NAME\Desktop\FOLDER\chromedriver.exe")
#For firefox
#driver = webdriver.Firefox(service=Service('D:\Projects\Selenium\geckodriver.exe'))
#For Chrome
driver = webdriver.Chrome(service=Service('D:\Projects\Selenium\chromedriver.exe'))



driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)
driver.close()