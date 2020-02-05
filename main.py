from PNZGUParser import PNZGUParser


def main():
    login = ''
    password = ''
    parser = PNZGUParser(login, password)
    parser.start()
