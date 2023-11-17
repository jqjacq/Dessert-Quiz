import random
from qna import questions 
from string import ascii_lowercase

num_correct = 0
num_questions_per_round = 10
all_questions = min(num_questions_per_round, len(questions))
randomize_questions = random.sample(list(questions.items()), all_questions)

for num, (question, multiple_choices) in enumerate(randomize_questions, start=1):
    # Print question and multiple choices
    print(f"Question {num}: {question}")
    correct_answer = multiple_choices[0] #All correct answers are in index 0
    sorted_answers = dict( #Randomize the order of multiple choices
        zip(ascii_lowercase, random.sample(multiple_choices, len(multiple_choices)))
    )
    for choice, multiple_choices in sorted_answers.items(): #Enumerate to get index of multiple_choices
        print(f" {choice}) {multiple_choices}") 
    
    # Retrieve user input and check if it is a valid answer. If not, ask again
    user_answer = input("Enter your answer: ")
    while user_answer not in sorted_answers:
        print(f"Invalid answer. Please choose either a, b, c, or d")
        user_answer = input("Enter your answer: ")

    # Retrieve user input and check if it's correct
    answer = sorted_answers[user_answer]
    if answer == correct_answer:
        num_correct += 1
        print(f"✔️  Correct!😁")
    else:
        print(f"✖️  Incorrect!😭 The correct answer is {correct_answer}")

print(f"\nYou got {num_correct} correct out of {num} questions")