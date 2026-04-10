import csv
import json
import os 

class card():
    
    def __init__(self, question, correct_answer, num_incorrect=None, num_correct=None):
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

def pull_json():
    json_file = "cards.json"

    if os.path.exists(os.path.join(".", json_file)):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            return(data)
        except json.JSONDecodeError:
            return(None)
    else:
        return(None)

def push_json(data):
    with open('cards.json', 'w')as f:
        json.dump(data, f) 
    return

def file_read():
    with open("test.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        data_list = []

        for row in csv_reader:
            data_list.append(row)
    return(data_list)

def main():
    dict_list = None
    dump_arr = []

    if pull_json() == None:
        dict_list = file_read()    
        
        for dict in dict_list:
            dict = card(dict['question'],dict['correct_answer'])
            dict.ask()
            dump_arr.append(dict.dump())
           
    else: 
        dict_list = pull_json()

        for dict in dict_list: #there is some problems here if JSON exists then we need slightly different logic so we need to split them out to solve the error
            dict = card(dict['question'],dict['correct_answer'],dict['num_incorrect'],dict['num_correct'])
            dict.ask()
            dump_arr.append(dict.dump())

    push_json(dump_arr)

if __name__ == "__main__":
    main()

