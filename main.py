import csv
from os import wait

def file_read():

    with open("test.csv", "r") as file:
        csv_reader = csv.DictReader(file)

        data_list = []

        for row in csv_reader:
            data_list.append(row)
        
        return(data_list)

def data_cleaner(data):
    return

def main():
    dict_list = file_read()    
    
    for dict in dict_list:
        answer = input(f"Question: {dict['question']}\n")
        if answer == dict['correct_answer']:
            print(f"your answer {answer} was correct! Good job!")
        else: 
            print(f"your answer {answer} was incorrect! The correct answer was {dict['correct_answer']}!")

if __name__ == "__main__":
    main()
