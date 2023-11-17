# import questions from qna.py
from qna import questions 
from string import ascii_lowercase

# Loop through questions and multiple choices
for num, (question, multiple_choices) in enumerate(questions.items(), start=1):
    print(f"Question {num}: {question}")
    correct_answer = multiple_choices[0] #All correct answers are in index 0
    sorted_answers = dict(zip(ascii_lowercase, sorted(multiple_choices))) 

    for choice, multiple_choices in sorted_answers.items(): #Enumerate to get index of multiple_choices
        print(f" {choice}) {multiple_choices}") 
    
    # Retrieve user input and check if it's correct
    user_answer = input("Enter your answer: ")
    answer = sorted_answers.get(user_answer)

    if answer == correct_answer:
        print("✔️  Correct!😁")
    else:
        print("✖️  Incorrect!😭")
        print(f"The correct answer is {correct_answer}")