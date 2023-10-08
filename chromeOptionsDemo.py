# from selenium import webdriver
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximize")
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--ignore-certificate-errors ")
#
# driver = webdriver.Chrome(r"D:\Projects\Selenium\chromedriver.exe")
# driver.implicitly_wait(5)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# print(driver.title)


from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(r"D:\Projects\Selenium\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)