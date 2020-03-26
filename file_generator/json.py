import json


def create(file, data):
    with open(file, 'w') as file:
        json.dump(data, file)
