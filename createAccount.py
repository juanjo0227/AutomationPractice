import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

class CreateAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C://Users//USER//proyectos//selenium//assertions//chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://automationpractice.com/")

    def test_user_clicks_on_sign_in(self):
        login_button = self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        login_button.click()
    
    def test_user_enters_email(self):
        email_field = self.driver.find_element_by_name('email_create')
        email_field.clear()
        email_field.send_keys('juanjoserodriguezduque@gmail.com')

    def test_user_clicks_create_an_account(self):
        createAccount_button = self.driver.find_element_by_id('SubmitCreate')
        createAccount_button.click()

    def test_user_fill_sign_up_form(self):
        driver = self.driver

        title = driver.find_element_by_id('id_gender1')
        title.click()
        
        first_name = driver.find_element_by_name('customer_firstname')
        first_name.clear()
        first_name.send_keys('Juan José')
        last_name = driver.find_element_by_name('customer_lastname')
        last_name.clear()
        last_name.send_keys('Rodríguez')



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'createAccount-report'))