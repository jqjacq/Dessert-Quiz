# import questions from qna.py
from qna import questions 


for question, multiple_choices in questions.items():
    #Print & randomize the answers using enumerate
    correct_answer = multiple_choices[0] #All correct answers are in index 0
    sorted_answers = sorted(multiple_choices) #Sorts answers in alphabetical order
    for num, multiple_choices in enumerate(sorted_answers):
        print(f" {num + 1}) {multiple_choices}")

    # Retrieve user input and check if it's correct
    get_user_input = int(input(f"\n{question}\n")) 
    answer = sorted_answers[get_user_input]
    if answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {correct_answer}")


    