import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from appium import webdriver
from config.test_des_cap import get_des_cap
import pytest

# from report.report import generate_report #gen te report in txt file #python -m unittest tests.test_login

###################################################################
# ##pytest --html=reports/test_report.html --self-contained-html  #
# ## run all testt case and got html file                         #
###################################################################

appium_server_url = 'http://127.0.0.1:4723'
capabilities_options = UiAutomator2Options().load_capabilities(get_des_cap())


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_open_app(self) -> None:
        try:
            self.driver.implicitly_wait(20)
            element = self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Continue with Google\"]")

            # Assert that the element is found
            assert element is not None, "Element not found"

            # Assert that the element's text matches the expected value
            assert element.text == "Continue with Google", f"Expected text 'Continue with Google', but found '{element.text}'"

            print("Test Passed: Element is found and text is correct.")

        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    if __name__ == '__main__':
        unittest.main()

    def test_login_correct(self) -> None:
        try:
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,
                                     "//A1.I0/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button").click()
            # result = "Click Login Successfully"

            # verify
            elements2 = self.driver.find_elements(By.XPATH,
                                                  "//A1.I0/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
            self.assertTrue(len(elements2) > 0, "Button not found after clicking")

        except Exception as e:
            self.fail(f"Test failed due to: {e}")


if __name__ == "__main__":
    unittest.main()
