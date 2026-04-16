import csv
import json

def file_read(filename):

    if '.' in filename:
        filename_arr = filename.split('.')
        filename = filename_arr[0] 

    file = filename + ".csv"
    try:
        with open(file, "r") as file:
            csv_reader = csv.DictReader(file)
            data_list = []
            for row in csv_reader:
                data_list.append(row)
        return(data_list)

    except FileNotFoundError:
      print(f"Error: that file {file} doesn't exist")
    return 

def build_deck(filename):

    id_counter = 0
    dump_arr = []
    data_list = file_read(filename)
    for card in data_list:
        card['num_incorrect'] = 0
        card['num_correct'] = 0
        card['id'] = id_counter
        dump_arr.append(card)
        id_counter += 1
    with open(filename + ".json", "w") as file:
        json.dump(dump_arr, file)
    return

if __name__ == "__main__":
    build_deck(input("What file do you wish to initialize?\n"))
