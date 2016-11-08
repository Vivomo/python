from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os

driver_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'


class Chrome(object):

    def __init__(self):
        self.driver = webdriver.Chrome(driver_path)

    def close(self):
        self.driver.quit()

