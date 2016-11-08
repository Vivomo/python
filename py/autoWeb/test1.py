from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os

driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.baidu.com')
time.sleep(5) # Let the user actually see something!
