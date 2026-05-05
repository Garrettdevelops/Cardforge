import pathlib
import platform
import json
import os 

class deck():
    def __init__(self, cards, id, scheduler):
        self.id = id
        self.cards = cards
        self.scheduler = scheduler or None
        return



class card():
    
    def __init__(self, question, correct_answer, num_incorrect=None, num_correct=None, id=None):
        self.id = id
        self.question = question
        self.correct_answer = correct_answer

        if num_incorrect == None:
            self.num_incorrect = 0
        else:
            self.num_incorrect = num_incorrect
       
        if num_correct == None:
            self.num_correct = 0
        else:
            self.num_correct = num_correct

        return

    def correctly_answered(self):
        self.num_correct += 1
        return
    
    def incorrectly_answered(self):
        self.num_incorrect += 1
        return

    def dump(self):
        dump_dict = {}
        dump_dict['question'] = self.question
        dump_dict['correct_answer'] = self.correct_answer
        dump_dict['num_incorrect'] = self.num_incorrect
        dump_dict['num_correct'] = self.num_correct
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

def init_cards(dict_list):
    card_list = []
    for dict in dict_list:
        dict = card(dict['question'],dict['correct_answer'],dict['num_incorrect'],dict['num_correct'])
        card_list.append(dict)
    return(card_list)

def check_answer(card, user_input):
    if user_input.lower() == card.correct_answer.lower():
        return(True)
    else: return(False)

def input_loop(card_list):

    for card in card_list:
        print(card.question)
        user_input = input()
        correct_status = check_answer(card, user_input)
        if correct_status == True:
            print("Correct!")
            card.correctly_answered()
        else:
            print(f"Incorrect, the correct answer is {card.correct_answer}")
            card.incorrectly_answered()

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

