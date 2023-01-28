"""
Below program was developed as a support to learing process. 
Program generates a set of test questions based on question and answers base located in excel file name "TEST.xlsx". 
Excel file contains 3 columns named: "question" - contains the content of the question, "posibilities" - contains options of answers (A, B, C, D) 
and "answer" - which contains the proper answer to the question.
Program display questions and check answers.


User specifies how many question he wants to answer. 
Then question is displayed, user put his answer to terminal and get notification if he is right or not. 
Correct answers are counted and displayed after the test. 
"""

import pandas as pd
import random

#CLASS FOR TEXT FORMATTING
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#IMPORT EXCEL FILE WITH TEST'S QUESTIONS AND ANSWERS
test = pd.read_excel("TEST.xlsx")

test_length = int(input("How many questions do you want to answer?\nPick number or '0' for all\n"))

#DEFINE TEST LENGTH AND PICK RANDOMLY NUMBERS AND QUESTION ORDER
if test_length > len(test):
    print(f"Out of range! Test contains only {len(test)} questions")

elif test_length == 0:
    question_numbers = random.sample(range(0,len(test)), len(test))

else:
    question_numbers = random.sample(range(0,len(test)), test_length)

print(question_numbers)

#TEST STARTS


points = 0
for question_number in question_numbers:
    question = test['question'][question_number]
    print(question)
    print(test['posibilities'][question_number]+'\n')

    user_answer = str(input()).upper()

    if user_answer == test['answer'][question_number]:
        print(f"{bcolors.OKCYAN}{bcolors.BOLD}GOOD!\n{bcolors.ENDC}")
        points += 1
    else:
        print(f"{bcolors.FAIL}{bcolors.BOLD}WRONG!\n{bcolors.ENDC}")

print(f"End of the test! You answer correct for {points} of {len(question_numbers)} questions!")