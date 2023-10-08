from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(service=Service('D:\Projects\Selenium\chromedriver.exe'))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
driver.maximize_window()
#Checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes :
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        time.sleep(1)

#RadioButton
Radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
for radiobutton in Radiobuttons:
    radiobutton.click()
    time.sleep(1)
    assert radiobutton.is_selected()

#allert
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Akash")
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alertText = alert.text

#alert.accept()
alert.dismiss()
time.sleep(2)
driver.close()