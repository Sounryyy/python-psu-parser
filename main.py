import threading
import time

from PNZGUParser import PNZGUParser

config = {
    'login': '',
    'password': '',
    'pages_amount': 9,
    'webdriver_link': '/Users/justtrueserj/PycharmProjects/python-psu-parser/chromedriver',
    'is_need_parse_employers_with_student_card': True
}


def main(cfg, iteration):
    time.sleep(iteration * 3)
    parser = PNZGUParser(cfg, iteration)
    parser.start()


def start_threads(page_number, amount):
    for thread_number in range(amount):
        thread = threading.Thread(target=main, args=(config, page_number + thread_number))
        thread.start()


if __name__ == "__main__":
    pageNumber = 0
    cycle_iterations = config['pages_amount'] + 1

    while pageNumber < cycle_iterations:
        if pageNumber == 0:
            pageNumber = 1

        if cycle_iterations - pageNumber == 1:
            print(1)
            pageNumber += 1
            main(config, pageNumber)

        if cycle_iterations - pageNumber == 2:
            print(2)
            start_threads(pageNumber, 2)
            pageNumber += 2

        if cycle_iterations - pageNumber >= 3:
            print(3)
            start_threads(pageNumber, 3)
            pageNumber += 3

        time.sleep(165)

