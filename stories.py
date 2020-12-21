from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from createAccount import CreateAccountTest
from login import LoginTest

createAccount_test = TestLoader().loadTestsFromTestCase(CreateAccountTest)
login_test = TestLoader().loadTestsFromTestCase(LoginTest)

smoke_test = TestSuite([createAccount_test, login_test])

kwargs = {
    "output": 'report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)