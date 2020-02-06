from PNZGUParser import PNZGUParser


def main():
    login = 's517658187'
    password = 'HzrYKkCB'
    is_need_parse_employers_with_student_card = True

    parser = PNZGUParser(login, password, is_need_parse_employers_with_student_card)
    parser.start()


if __name__ == "__main__":
    main()
