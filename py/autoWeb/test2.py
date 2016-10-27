from splinter.browser import Browser
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

browser = Browser('chrome', options=options)

browser.visit('http://www.google.com')
