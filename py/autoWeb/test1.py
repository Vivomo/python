from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Firefox()

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
#
# browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
#                            chrome_options=options)
browser.get('http://baidu.com')
