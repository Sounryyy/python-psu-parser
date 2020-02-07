from selenium import webdriver

from helpers import create_file


class PNZGUParser(object):

    def __init__(self, config, page_number):
        self.login = config['login']
        self.driver = webdriver.Chrome(config['webdriver_link'])
        self.password = config['password']
        self.page_number = page_number
        self.pages_amount = config['pages_amount']
        self.is_need_parse_employers_with_student_card = config['is_need_parse_employers_with_student_card']

    def start(self):
        self.open_PNZGU()
        self.login_in_PNZGU()
        self.start_parsing_cycle()

    def open_PNZGU(self):
        self.driver.get("https://www.pnzgu.ru/")

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

    def start_parsing_cycle(self):
        self.open_portfolio_employers_page()
        employers_dict = self.get_all_employers_dict_from_page()

        for employer in employers_dict:
            self.parse_employer(employer)

        print('done')

    def open_portfolio_employers_page(self):
        self.driver.get("https://lk.pnzgu.ru/portfolio/empl/p/" + str(self.page_number))

    def get_all_employers_dict_from_page(self):
        employers_dict = {}

        employers = self.driver.find_elements_by_xpath("//div[@style='display: flex;']")

        for employer in employers:
            employer_type = employer.find_element_by_tag_name('img').get_attribute('title')
            employer_id = employer.find_element_by_tag_name('a').get_attribute('href').split('/')[-1]

            if self.is_need_parse_employers_with_student_card:
                employers_dict[employer_id] = employer_type

            if not self.is_need_parse_employers_with_student_card and employer_type == 'Личная карточка сотрудника':
                employers_dict[employer_id] = employer_type

        return employers_dict

    def parse_employer(self, string_id):
        self.open_employer_rating(string_id)
        employer_data = self.get_employer_data()

        create_file(string_id, employer_data)

    def open_employer_rating(self, string_id):
        self.driver.get(f"https://lk.pnzgu.ru/rating/{string_id}")

    def get_employer_data(self):
        employer_data = []

        cells_list = self.get_cells_list_from_table()

        for cell in cells_list:
            employer_data.append(self.get_indicator_and_value(cell))

        return employer_data

    def get_cells_list_from_table(self):
        table = self.driver.find_element_by_tag_name('tbody')

        return table.find_elements_by_tag_name('tr')

    def get_indicator_and_value(self, cell):
        indicator, value, *other_elements = cell.find_elements_by_tag_name('td')

        return [indicator.text, value.text]

