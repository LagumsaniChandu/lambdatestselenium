import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

username = os.getenv("lagumsanichandu")  # Replace the username
access_key = os.getenv("l3Yn2Wc9KZZXhtCgE2VdQOw1YVLJjOfca4LDynykqYae3ftU9S")


class FirstSampleTest(unittest.TestCase):
    def setUp(self):
        single_test = {
            'LT:Options': {
                "username": "lagumsanichandu",
                "accessKey": "l3Yn2Wc9KZZXhtCgE2VdQOw1YVLJjOfca4LDynykqYae3ftU9S",
                "video": True,
                "platformName": "Windows 10",
                "resolution": "1920x1080",
                "network": True,
                "build": "selenium",
                "name": "python",
                "selenium_version": "4.0.0",
                "driver_version": "108.0",
                "w3c": True,
                "plugin": "python-pytest"
            },
            "browserName": "Chrome",
            "browserVersion": "108.0",
        }

        self.driver = webdriver.Remote(
             command_executor="https://lagumsanichandu:l3Yn2Wc9KZZXhtCgE2VdQOw1YVLJjOfca4LDynykqYae3ftU9S@hub.lambdatest.com/wd/hub".format(
             username, access_key),
             desired_capabilities=single_test)

    def tearDown(self):
        self.driver.quit()


    def test_demo_site(self):
        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

    # Url
        print('Loading URL')
        driver.get("https://www.lambdatest.com/selenium-playground/")

    # chrome_path = Service(r'C:\Drivers\chromedriver_win32\chromedriver.exe')
    # driver = webdriver.Chrome(service=chrome_path)
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()
        time.sleep(4)

        elem = driver.find_element(By.XPATH, "//*[@id='slider3']/div/input")
        ActionChains(driver).drag_and_drop_by_offset(elem, 120, 0).perform()

        slidder = driver.find_element(By.XPATH, "//*[@id='rangeSuccess']").text
        assert "95" in slidder
if __name__ == "__main__":
    unittest.main()