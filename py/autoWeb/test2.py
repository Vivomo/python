from splinter.browser import Browser
from selenium import webdriver

chromeDriverPath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromeDriverPath)
driver.find_element_by_class_name('').f

driver.get('http://vimo.360jlb.cn')
