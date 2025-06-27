import random
import time
from quiz_exceptions import InvalidAnswerError
from quiz_questions import generate_question  # Import the question generator

# Step 1: Read user name and capture the time
name = input("Enter your name: ")
start_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"\nWelcome, {name}!")
print(f" You started the game at: {start_time}")
print("Let's start the quiz.\n")

score = 0
question_number = 1  # To track number of questions

while True:
    try:
        # Generate question and correct answer
        question, correct_answer = generate_question()
        
        # Record time before displaying the question
        question_start = time.time()
        
        print(f"Q{question_number}: {question}")
        user_input = input("Your answer: ")
        
        # Record time after answering
        question_end = time.time()
        time_taken = question_end - question_start
        
        if not user_input.isdigit():
            raise InvalidAnswerError()
        user_answer = int(user_input)

        # Check correctness
        if user_answer == correct_answer:
            print(" Correct!")
            score += 10
        else:
            print(f" Wrong! The correct answer is {correct_answer}.")
            score -= 5

        # Print score and time taken
        print(f" Current Score: {score}")
        print(f" Time taken to answer: {time_taken:.2f} seconds\n")

        question_number += 1

    except InvalidAnswerError as e:
        print(f" Error: {e}\n")
        continue

    # Ask if user wants to continue
    choice = input("Do you want to continue the quiz? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("\nLOOSER ")
    break