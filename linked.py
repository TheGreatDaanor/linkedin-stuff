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

    def search(self):
        s_bar = self.driver.find_element_by_xpath(
            '//*[@id="ember31"]/input')
        s_bar.send_keys('Recruiter')
        sleep(1)
        s_bar.submit()


bot = LinkedinBot()
sleep(1)
bot.login()
sleep(3)
bot.search()
