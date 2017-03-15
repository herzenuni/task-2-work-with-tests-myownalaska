import json

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:

        data = json.load(data_file)



except FileNotFoundError:

    print("Файл не найден! Файл должен называться: {}".format(filename))

    status = 'Файл не найден'


for li in data:
    print("_________________________________________________________")
    print("company: {}".format(li['company']))
    print("email: {}".format(li['email']))
    print("phone: {}".format(li['phone']))
    print("address: {}".format(li['address']))