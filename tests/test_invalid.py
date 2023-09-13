import time
import unittest
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from small_automation.utils.Driver_setup import driver_setup
from selenium.webdriver.common.by import By



from small_automation.src.common.actions import TestLogin
class Tests(TestLogin):
    def test_contact_us_without_firsname(self):
     contact_button = self.my_driver.find_element(By.XPATH, '//*[@id="menu-item-25"]/a/span[2]')
     contact_button.click()
     time.sleep(2)
     input_last_name = self.my_driver.find_element(By.XPATH, '//*[@id="post-24"]/div/div/form/div[2]/input')
     input_last_name.send_keys('kahala')
     input_email = self.my_driver.find_element(By.XPATH, '//*[@id="post-24"]/div/div/form/div[3]/input')
     input_email.send_keys('2010@gmail.com')
     input_content = self.my_driver.find_element(By.XPATH, '//*[@id="post-24"]/div/div/form/div[4]/textarea')
     input_content.send_keys('very nice')
     input_submit = self.my_driver.find_element(By.XPATH, '//*[@id="post-24"]/div/div/form/div[7]/button/div')
     input_submit.click()
     time.sleep(2)
