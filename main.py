from PNZGUParser import PNZGUParser


def main():
    config = {
        'login': 's517658187',
        'password': 'HzrYKkCB',
        'pages_amount': 3,
        'is_need_parse_employers_with_student_card': True,
    }

    parser = PNZGUParser(config)
    parser.start()


if __name__ == "__main__":
    main()
