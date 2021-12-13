from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):
    baseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    lp = LoginPage(driver)

    def test_validLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("test@gmail.com", "abcabc")
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()


    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failure")

        self.driver.quit()

