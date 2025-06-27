import random

perfect_squares = [i * i for i in range(1, 101)]  # 1^2 to 100^2

def generate_question():
    question_type = random.choice(["square", "square_root"])

    if question_type == "square":
        number = random.randint(1, 100)
        question = f"What is the square of {number}?"
        answer = number ** 2
    else:
        number = random.choice(perfect_squares)
        question = f"What is the square root of {number}?"
        answer = int(number ** 0.5)

    return question,answer