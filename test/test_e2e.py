from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        # Navigate to "Shop"
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                # add Item in the cart
                product.find_element(By.XPATH, "div/button").click()
                print(product.find_element(By.XPATH, "div/button").text)

        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-success']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ind")
        time.sleep(2)

       #verefying text India
        self.verefyLinkPresent("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        success = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        assert "Success! Thank you!" in success

        # driver.get_screenshot_as_file("screen.png")
        time.sleep(3)


