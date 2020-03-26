import csv


def create(file, data):
    with open(file, 'w') as file:
        keys = data.keys()
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerow(data)
