import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class A1_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_navigation(self):
        driver = self.driver
        driver.get ("https://www.a1.digital")

        # accept all cookies, can be dropped if cookies already accepted or not wanted
        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
        finally:
            driver.find_element_by_id("onetrust-accept-btn-handler").click()
            

        try:
            element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Lösungen")))
        finally:
            driver.find_element_by_link_text("Lösungen").click()
            

        try:
            element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Exoscale: Die Europäische Cloud Infrastruktur")))
        finally:
            driver.find_element_by_link_text("Exoscale: Die Europäische Cloud Infrastruktur").click()
            




if __name__ == "__main__":
    unittest.main()
