import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
import os

driver_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'


class Task(object):

    def __init__(self, options):
        self.driver = webdriver.Chrome(driver_path)
        self.domain = options['domain']
        self.wait = WebDriverWait(self.driver, 10)

    @staticmethod
    def dom_ready(driver):
        state = driver.execute_script('return document.readyState')
        return state == 'complete'

    def event_signup(self, event_id):
        driver = self.driver
        driver.get('%s/event?id=%s' % (self.domain, event_id))
        self.wait.until(self.dom_ready)
        apply_elem = driver.find_element_by_class_name('join')
        apply_elem.click()
        # TODO 填值 报名

    def login(self, username, password):
        driver = self.driver
        login_url = self.domain + '/login'
        driver.get(login_url)
        form = driver.find_element_by_class_name('loginform')
        e_username = form.find_element_by_name('username')
        e_password = form.find_element_by_name('password')
        e_username.send_keys(username)
        e_password.send_keys(password)
        form.submit()
        time.sleep(2)

task = Task({
    'domain': 'http://vm.360jlb.cn'
})
with open('../src/ignore/data.json', 'r', encoding='utf-8') as jsonFile:
    data = json.loads(jsonFile.read())
task.login(data['username'], data['password'])
task.event_signup(35712)
