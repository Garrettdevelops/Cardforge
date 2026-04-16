import csv
import json
import os 

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

    def ask(self):
        answer = input(f"Quesiton: {self.question}\n")

        if answer == self.correct_answer:
            print(f"Correct!")
            self.correctly_answered()
        else:
            print(f"Incorrect, the correct answer is {self.correct_answer}")
            self.incorrectly_answered()
        return

def pull_json(filename):
    if filename == None:
        json_file = "cards.json"
    else:
        json_file = filename + ".json"

    if os.path.exists(os.path.join(".", json_file)):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            return(data)
        except json.JSONDecodeError:
            return(None)
    else:
        return(None)

def push_json(data, filename):
    if filename == None:
        filename = 'cards.json'
    else: filename = filename + ".json"

    with open(filename, 'w')as f:
        json.dump(data, f) 
    return

def run_flashcards(filename=None):
    if filename == None:
        filename = "test"

    if '.' in filename:
        filename_arr = filename.split('.')
        filename = filename_arr[0] 

    if pull_json(filename) == None:
        print("that file has not been initialized yet")
        return
    else: 
        dict_list = pull_json(filename)

    dump_arr = []
    for dict in dict_list:
        dict = card(dict['question'],dict['correct_answer'],dict['num_incorrect'],dict['num_correct'])
        dict.ask()
        dump_arr.append(dict.dump())
    push_json(dump_arr, filename)


if __name__ == "__main__":
    run_flashcards()

