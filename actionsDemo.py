from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(r"D:\Projects\Selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.thedailystar.net/")

#ActionsChains
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//li[@aria-label='News']//a[normalize-space()='News']")).perform()
time.sleep(3)
action.move_to_element(driver.find_element(By.XPATH,"//li[@role='menuitem']//a[normalize-space()='Asia']")).click()

time.sleep(3)