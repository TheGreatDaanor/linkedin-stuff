from selenium import webdriver
from time import sleep

from secrets import username, password


class LinkedinBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.linkedin.com/login')

        si_email = self.driver.find_element_by_xpath('//*[@id="username"]')
        si_email.click()
        si_email.send_keys(username)

        si_pass = self.driver.find_element_by_xpath('//*[@id="password"]')
        si_pass.click()
        si_pass.send_keys(password)

        si_btn = self.driver.find_element_by_xpath(
            '//*[@id="app__container"]/main/div/form/div[3]/button')
        si_btn.click()

    def connect(self):
        sres = self.driver.find_elements_by_class_name("search-results-container")
        sresi = self.driver.find_elements_by_class_name("search-result__wrapper")
        sline = self.driver.find_elements_by_class_name("subline-level-1")
        cbtn = self.driver.find_elements_by_class_name("search-result__action-button")

        while sresi in sres:
            if sline in sresi:
                if "Cyber Security Recruiter" in sline:
                    cbtn.click()
                else:
                    break


bot = LinkedinBot()
sleep(1)
bot.login()
sleep(3)
bot.search()
sleep(2)
bot.connect()
