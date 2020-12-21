import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class CreateAccountTest(unittest.TestCase):
    
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

        first_name_1 = driver.find_element_by_name('customer_firstname')
        first_name_1.clear()
        first_name_1.send_keys('Juan José')

        last_name_1 = driver.find_element_by_name('customer_lastname')
        last_name_1.clear()
        last_name_1.send_keys('Rodríguez')

        email = driver.find_element_by_id('email')
        email.clear()
        email.send_keys('juanjoserodriguezduque@gmail.com')

        password = driver.find_element_by_id('passwd')
        password.clear()
        password.send_keys('1234567890')

        email = driver.find_element_by_id('email')
        email.clear()
        email.send_keys('juanjoserodriguezduque@gmail.com')

        days = Select(self.driver.find_element_by_id('days'))
        days.select_by_index(27)

        months = Select(self.driver.find_element_by_id('months'))
        months.select_by_index(2)

        first_name_2 = driver.find_element_by_id('firstname')
        first_name_2.clear()
        first_name_2.send_keys('Juan José')

        last_name_2 = driver.find_element_by_id('lastname')
        last_name_2.clear()
        last_name_2.send_keys('Rodríguez')

        company = driver.find_element_by_id('company')
        company.clear()
        company.send_keys('Freelance')

        address_1 = driver.find_element_by_id('address1')
        address_1.clear()
        address_1.send_keys('797-799 5th Ave')

        address_2 = driver.find_element_by_id('address2')
        address_2.clear()
        address_2.send_keys('Apartment 1001')

        city = driver.find_element_by_id('city')
        city.clear()
        city.send_keys('New York')

        state = Select(self.driver.find_element_by_id('id_state'))
        state.select_by_index(33)

        postal_code = driver.find_element_by_id('postcode')
        postal_code.clear()
        postal_code.send_keys('10016')

        country = Select(self.driver.find_element_by_id('id_country'))
        country.select_by_index(1)

        additional_information = driver.find_element_by_name('other')
        additional_information.clear()
        additional_information.send_keys('Thank you!')

        home_phone = driver.find_element_by_name('phone')
        home_phone.clear()
        home_phone.send_keys('5864139')
        
        mobile_phone = driver.find_element_by_name('phone_mobile')
        mobile_phone.clear()
        mobile_phone.send_keys('+57 3045385895')

        alias = driver.find_element_by_name('alias')
        alias.clear()
        alias.send_keys('juanjo')

        register_button = driver.find_element_by_name('submitAccount')
        register_button.click()

    def test_user_is_taken_my_account_page(self):
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
        unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'createAccount-report'))