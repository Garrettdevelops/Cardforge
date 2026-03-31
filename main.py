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
        for key in dict:
            answer = input(f"Question: {key}")
            if answer == dict[key]:
                print(f"your answer {answer} was correct!")
            else:
                print(f"your answer {answer} was incorrect! The correct answer is {dict[key]}.")

if __name__ == "__main__":
    main()

 #
 #   if answer == correct_answer:
#
 #   else: 

   #answer = input(question + "\n")
