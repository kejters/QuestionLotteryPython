import pandas as pd
import random


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


def choose_category(file):

    list_of_categories = sorted(list(set(file['cat'])))
    print("You have below categories to chose:")
    cat_number = 0
    for category in list_of_categories:
        cat_number += 1
        print(f'{cat_number} - {category}')
    print(f'{cat_number + 1} - All')

    chosen_category = int(input('Which one do you want to choose? '))

    if chosen_category == len(list_of_categories) + 1:
        filter_file = file
    else:
        filter_file = file[(file['cat'] == list_of_categories[chosen_category - 1])]

    return filter_file


def choose_test_length(filtered_category):
    test_length = int(input(f"There is {len(filtered_category)} questions in this category. How many questions do you want to answer?\nPick number or '0' for all\n"))

    if test_length > len(filtered_category):
        return print(f"Out of range! Test contains only {len(filtered_category)} questions")

    elif test_length == 0:
        return random.sample(list(filtered_category['No']), len(filtered_category))

    else:
        return random.sample(list(filtered_category['No']), test_length)


def test_closed_questions(file_name):

    test = pd.read_excel(file_name)
    filter_questions = choose_category(test)
    questions = choose_test_length(filter_questions)

    points = 0
    for question_number in questions:
        question = test['question'][question_number]
        print(question)
        print(test['posibilities'][question_number] + '\n')

        user_answer = str(input()).upper()

        if user_answer == test['answer'][question_number]:
            print(f"{bcolors.OKCYAN}{bcolors.BOLD}GOOD!\n{bcolors.ENDC}")
            points += 1
        else:
            print(f"{bcolors.FAIL}{bcolors.BOLD}WRONG!\n{bcolors.ENDC}")

    print(f"End of the test! You answer correct for {points} of {len(questions)} questions!")


def test_open_questions(file_name):

    test = pd.read_excel(file_name)
    filter_questions = choose_category(test)
    questions = choose_test_length(filter_questions)

    for question_number in questions:
        question = test['question'][question_number]
        print(f"{bcolors.BOLD}{question}\n{bcolors.ENDC}")
        user_answer = str(input("To show answer type ENTER. For exit type Q\n").upper())
        if user_answer == "Q":
            break
        print(f"{test['answer'][question_number]}\n")
        input("Press ENTER to continue. For exit type Q\n")


test_type = int(input("Choose test type to start: \n 1. Closed questions test \n 2. Flashcards \n"))

if test_type == 1:
    test_closed_questions("TEST.xlsx")
elif test_type == 2:
    test_open_questions("OPEN.xlsx")
