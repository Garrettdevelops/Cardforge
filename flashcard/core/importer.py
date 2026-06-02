
import csv
import os
import json
import pathlib
import platform

def file_read(filename):


    file = filename + ".csv"
    try:
        with open(file, "r") as file:
            csv_reader = csv.DictReader(file)
            data_list = []
            for row in csv_reader:
                data_list.append(row)
        
        if "question" and "correct_answer" not in data_list[0]:
            raise Exception("an error occured", "the formatting of the csv is incorrect, please solve the formatting issue", 1)

        return(data_list)

    except FileNotFoundError:
        print(f"Error: that file {file} doesn't exist")
    return

def build_deck(filename):
    if '.' in filename:
        filename_arr = filename.split('.')
        filename = filename_arr[0] 

    path = initalize_storage()


    id_counter = 0
    dump_arr = []
    data_list = file_read(filename)

    for card in data_list:
        card['num_easy_answer'] = 0
        card['num_easy_answer'] = 0
        card['num_medium_answer'] = 0
        card['num_hard_answer'] = 0
        card['num_blank_answer'] = 0
        card['id'] = id_counter
        dump_arr.append(card)
        id_counter += 1
    with open(os.path.join(str(path), filename + ".json"), "w") as file:
        json.dump(dump_arr, file)
    print(f"Deck created: {filename}\n ")
    return

def initalize_storage():

    operating_system = platform.system() 
    storage_path = None

    if operating_system == "Darwin":
        storage_path = pathlib.Path("~/Library/Application Support/flashcard").expanduser()
    elif operating_system == "Windows":
        storage_path = pathlib.Path(os.path.expandvars("%APPDATA%/flashcard"))
    elif operating_system == "Linux":
        storage_path = pathlib.Path("~/.local/share/flashcard").expanduser()

    else:
        user_choice = input("os could not be understood, what OS are you running? (w)Windows, (m)Mac, (l)Linux, (o)Other:") 
        if user_choice == "w":
            storage_path = pathlib.Path(os.path.expandvars("%APPDATA%/flashcard"))
        elif user_choice == "m":
            storage_path = pathlib.Path("~/Library/Application Support/flashcard").expanduser()
        elif user_choice == "l":
            storage_path = pathlib.Path("~/.local/share/flashcard").expanduser
        elif user_choice == "o":
            print("please submit a bug report on github and state your operating system.  I will try to fix the bug as soon as possible.")  
        else: 
            print("that was an invalid choice")

    storage_path.mkdir(parents=True, exist_ok=True)

    return(storage_path)

if __name__ == "__main__":
    build_deck(filename="test")

