import time
import  unittest
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from utils import Driver_setup
from utils.Driver_setup import driver_setup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select




class TestLogin(TestCase):

    def setUp(self) -> None:
         self.my_driver = driver_setup()
         self.my_driver.get('https://thedemosite.co.uk/')

    def tearDown(self):
        # Clean up: Close the WebDriver
        time.sleep(1)
        self.my_driver.quit()

    if __name__ == "__main__":

        unittest.main()