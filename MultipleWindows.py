from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service('D:\Projects\Selenium\chromedriver.exe'))
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Click Here").click()
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
parent_window = driver.window_handles[0]
driver.switch_to.window(parent_window)
print(driver.find_element(By.TAG_NAME,"h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text


time.sleep(2)
driver.close()