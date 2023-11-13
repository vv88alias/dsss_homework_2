import random
def random_number_generator(min_value, max_value):
    """
    Random integer will be generate between min and max value.

    Args:
        min_value (int): minimum value of random number
        max_value (int): maximum value of random number
    Returns:
        int: random number between min and max value
    """
    return random.randint(int(min_value), int(max_value))
def random_operator():
    """
        Random operator will be chosen among '+', '-', '*'.

        Args:
            None
        Returns:
            str: random operator
    """
    return random.choice(['+', '-', '*'])
def calculation(number1, number2, operator):
    """
        Calculation will be done based on the operator and two numbers.

        Args:
            number1 (int): first number
            number2 (int): second number
            operator (str): operator
        Returns:
            problem(str): formular of calculation
            answer(int): result of calculation
    """
    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem, answer

def math_quiz():
    """
        Math quiz game will be played.It will first print out the welcome message and rules.
        Then, it will generate random numbers and operator.
        It will ask user to input the answer. If the answer is correct, it will print out the correct message and add 1 point to the score.
        If the answer is wrong, it will print out the correct answer.
        After three questions, it will print out the final score.

        Args:
            None
        Returns:
            str: final score
    """
    scores = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(total_questions):
        number1 = random_number_generator(1, 10);
        number2 = random_number_generator(1, 5.5);
        operator = random_operator()

        problem, answer = calculation(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct! You earned a point.")
                scores += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nGame over! Your score is: {scores}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
