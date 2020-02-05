from selenium import webdriver


class PNZGUParser(object):

    def __init__(self):
        self.driver = webdriver.Chrome('/Users/justtrueserjdev/Downloads/chromedriver')

    def parse(self):
        self.login_in_PNZGU()
        self.go_to_lk()
        self.parse_h1()

    def login_in_PNZGU(self):
        self.driver.get("https://www.pnzgu.ru/")

        lk_button = self.driver.find_element_by_class_name("link-btn-lk")
        login_field = self.driver.find_element_by_name('name')
        password_field = self.driver.find_element_by_name('password')
        authorization_button = self.driver.find_element_by_name('login')

        lk_button.click()

        login_field.send_keys('s517658187')
        password_field.send_keys('HzrYKkCB')

        authorization_button.click()

    def go_to_lk(self):
        self.driver.get("https://lk.pnzgu.ru/portfolio/my")

    def parse_h1(self):
        tryS = self.driver.find_element_by_tag_name('h1')
