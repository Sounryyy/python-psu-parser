from selenium import webdriver


class PNZGUParser(object):

    def __init__(self, login, password):

        self.driver = webdriver.Chrome('/Users/justtrueserjdev/Downloads/chromedriver')
        self.output_file = open('output.txt', 'w')
        self.login = login
        self.password = password

    def start(self):

        self.open_PNZGU()
        self.login_in_PNZGU()
        self.go_to_lk()
        self.parse_h1()

    def open_PNZGU(self):

        self.driver.get("https://www.pnzgu.ru/")

    def save_in_file(self, text):

        self.output_file.write(text)

    def login_in_PNZGU(self):

        lk_button = self.driver.find_element_by_class_name("link-btn-lk")

        if lk_button.text == 'Личный кабинет':
            login_field = self.driver.find_element_by_name('name')
            password_field = self.driver.find_element_by_name('password')
            authorization_button = self.driver.find_element_by_name('login')

            lk_button.click()

            login_field.send_keys(self.login)
            password_field.send_keys(self.password)

            authorization_button.click()

    def go_to_lk(self):

        self.driver.get("https://lk.pnzgu.ru/portfolio/my")

    def parse_h1(self):

        parsed_h1 = self.driver.find_element_by_tag_name('h1').text

        self.save_in_file(parsed_h1)

