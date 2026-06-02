import random
import pathlib
import platform
import json
import os 

class card():
    
    def __init__(self, question, correct_answer, num_easy_answer=None, num_medium_answer=None, num_hard_answer=None, num_blank_answer=None, id=None):
        self.id = id
        self.question = question
        self.correct_answer = correct_answer

        if num_easy_answer == None:
            self.num_easy_answer = 0
        else:
            self.num_easy_answer = num_easy_answer

        if  num_medium_answer == None:
            self.num_medium_answer = 0
        else:
            self.num_medium_answer = num_medium_answer


        if num_hard_answer == None:
            self.num_hard_answer = 0
        else:
            self.num_hard_answer = num_hard_answer


        if num_blank_answer == None:
            self.num_blank_answer = 0
        else:
            self.num_blank_answer = num_blank_answer    


        return

    def easy_answer(self):
        self.num_easy_answer += 1
        return
 
    def medium_answer(self):
        self.num_medium_answer += 1
        return
   
    def hard_answer(self):
        self.num_hard_answer += 1
        return

    def blank_answer(self):
        self.num_blank_answer += 1
        return

    def dump(self):
        dump_dict = {}
        dump_dict['question'] = self.question
        dump_dict['correct_answer'] = self.correct_answer
        dump_dict['num_easy_answer'] = self.num_easy_answer
        dump_dict['num_medium_answer'] = self.num_medium_answer
        dump_dict['num_hard_answer'] = self.num_hard_answer
        dump_dict['num_blank_answer'] = self.num_blank_answer
        return(dump_dict)


def find_path():

    operating_system = platform.system() 
    storage_path = None

    if operating_system == "Darwin":
        storage_path = pathlib.Path("~/Library/Application Support/flashcard").expanduser()
    elif operating_system == "Windows":
        storage_path = pathlib.Path(os.path.expandvars("%APPDATA%/flashcard"))
    elif operating_system == "Linux":
        storage_path = pathlib.Path("~/.local/share/flashcard").expanduser()

    storage_path.mkdir(parents=True, exist_ok=True)
 
    return(storage_path)



def pull_json(filename):
    storage_path = find_path()
    json_file = filename + ".json"

    if os.path.exists(os.path.join(str(storage_path),json_file)):
        try:
            with open(os.path.join(str(storage_path),json_file), 'r') as f:
                data = json.load(f)
            return(data)
        except json.JSONDecodeError:
            return(None)
    else:
        return(None)

def push_json(data, json_file):
    json_file = json_file + ".json"
    storage_path = find_path()

    with open(os.path.join(str(storage_path),json_file), 'w')as f:
        json.dump(data, f) 
    return

def results(dump_arr):
    title_string = ""
    value_string = ""
    for dict in dump_arr:
        if title_string == "":
            for key in dict.keys():
                title_string = title_string + " | " + key
            print(title_string)

        for value in dict.values():
            value_string = value_string + " | " + str(value)
        print(value_string)
        value_string= ""

def init_cards(dict_list):
    card_list = []
    for dict in dict_list:
        dict = card(dict['question'],dict['correct_answer'],dict['num_easy_answer'],dict['num_medium_answer'],dict['num_hard_answer'],dict['num_blank_answer'])
        card_list.append(dict)
        random.shuffle(card_list)
    return(card_list)

def check_answer(card, user_input):
    print(f"The correct answer is {card.correct_answer}")
    print(user_input)
    difficulty_answered = False

    while difficulty_answered == False:
        difficulty_rating = input("Rate the question's difficulty 1-4, one being instantly remembered and 4 being no idea\n")
        try:
            if type(difficulty_rating) != int:
                difficulty_rating = int(difficulty_rating)

            if difficulty_rating < 1 or difficulty_rating > 4:
                print(f"Invalid entry {difficulty_rating} cannot be accepted, please input an integer between 1 and 4")
                continue
                    
            difficulty_answered = True
            return(difficulty_rating)

        except ValueError:
            print(f"Invalid entry, you must type an integer.  Please try again")

def input_loop(card_list):

    for card in card_list:
        print(card.question)
        user_input = input()
        correct_status = check_answer(card, user_input)
        if correct_status == 1:
            card.easy_answer()
        elif correct_status == 2:
            card.medium_answer()

        elif correct_status == 3:
            card.hard_answer()

        elif correct_status == 4:
            card.blank_answer()

def dump_card_list(card_list):
    dump_arr = []
    for card in card_list:
        dump_arr.append(card.dump())
    return(dump_arr)

def run_flashcards(filename, verbose=False):
    if '.' in filename:
        filename_arr = filename.split('.')
        filename = filename_arr[0] 

    if pull_json(filename) == None:
        print("that file has not been initialized yet")
        return
    else: 
        dict_list = pull_json(filename)

    card_list = init_cards(dict_list) 
    input_loop(card_list)
    dump_arr = dump_card_list(card_list) 
    push_json(dump_arr,filename)

    if  verbose:
        results(dump_arr)


if __name__ == "__main__":
    run_flashcards("test", verbose=True)

