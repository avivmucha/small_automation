from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
options = ChromeOptions()
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
#
#
#
#
def driver_setup():
  options = ChromeOptions()
  service = ChromeService(ChromeDriverManager().install())
  options.add_experimental_option('detach', True)
  driver = webdriver.Chrome(service=service, options=options)
  return driver
