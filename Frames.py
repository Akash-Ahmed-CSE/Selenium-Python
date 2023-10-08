from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(service=Service('D:\Projects\Selenium\chromedriver.exe'))
driver.implicitly_wait(5)
#iframe, frameset, frame
driver.get("https://the-internet.herokuapp.com/iframe")

driver.maximize_window()

#frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()
time.sleep(2)
print(driver.find_element(By.TAG_NAME,"h3").text)
