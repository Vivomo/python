from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os

driver_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'


class Task(object):

    def __init__(self, options):
        self.driver = webdriver.Chrome(driver_path)
        self.domain = options['domain']

    def event_signup(self):
        pass

    def login(self, username, password):
        driver = self.driver
        login_url = self.domain + '/login'
        driver.get(login_url)
        time.sleep(2)
        form = driver.find_element_by_class_name('loginform')
        e_username = form.find_element_by_name('username')
        e_password = form.find_element_by_name('password')
        e_username.send_keys(username)
        e_password.send_keys(password)
        form.submit()

task = Task({
    'domain': 'http://vimo.360jlb.cn'
})
task.login('929992114@qq.com', '000000')
