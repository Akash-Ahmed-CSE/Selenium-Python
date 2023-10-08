from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


#webdriver.Chrome(r"C:\Users\USER_NAME\Desktop\FOLDER\chromedriver")
list1 = []
list2 = []
driver = webdriver.Chrome(r"D:\Projects\Selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

window = driver.window_handles[1]
driver.switch_to.window(window)
print(driver.find_element(By.TAG_NAME,'h3').text)
time.sleep(3)