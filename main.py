import threading
import time

from PNZGUParser import PNZGUParser


def main(cfg, iteration):
    time.sleep(iteration * 3)
    parser = PNZGUParser(cfg, iteration)
    parser.start()


def start_threads(page_number, amount):
    for thread_number in range(amount):
        thread = threading.Thread(target=main, args=(config, page_number + thread_number))
        thread.start()


if __name__ == "__main__":
    config = {
        'login': '',
        'password': '',
        'pages_amount': 7,
        'webdriver_link': '/Users/justtrueserjdev/Downloads/chromedriver',
        'is_need_parse_employers_with_student_card': True
    }

    cycle_iterations = config['pages_amount'] + 1
    for page in range(cycle_iterations):
        if page == 0:
            page += 1

        if cycle_iterations - page == 1:
            main(config, page)

        if cycle_iterations - page == 2:
            print(2)
            start_threads(page, 2)
            page += 1

        if cycle_iterations - page >= 3:
            print(1)
            start_threads(page, 3)
            page += 2

        time.sleep(250)
