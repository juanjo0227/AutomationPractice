import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C://chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://automationpractice.com/")

    def test_user_clicks_on_sign_in(self):
        sign_in_button = self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        sign_in_button.click()

    def test_user_enters_email(self):
        email_login = self.driver.find_element_by_id('email')
        email_login.clear()
        email_login.send_keys('juanjoserodriguezduque@gmail.com')
    
    def test_user_enters_password(self):
        password_login = self.driver.find_element_by_xpath('//*[@id="passwd"]')
        password_login.clear()
        password_login.send_keys('1234567890')

    def test_user_clicks_sign_in(self):
        submit_login = self.driver.find_element_by_id('SubmitLogin')
        submit_login.click()

    def test_the_user_is_successfully_logged_in(self):
        self.assertTrue(self.is_element_present(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span'))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True
    

if __name__ == "__main__":
        unittest.main(verbosity = 2)