import csv


def create_file(file_name, data):
    file = open(f"{file_name}.csv", 'w')
    with file:
        writer = csv.writer(file)
        writer.writerows(data)
