import random

def random_integer(min, max):
    """
    choose a random integer.

    args:
    min (int): lower bound of the integer
    max (int): upper boung of the integer

    returns:
    int: random int
    """
    return random.randint(min, max)

def random_operator():
   """
   choosing a random operator.
   
   args:

   returns:
   string: random operator
   """
   return random.choice(['+', '-', '*'])

def formula_builder(num1, num2, operator):
    """
    building a random formula.

    args:
    n1 (int): first number of formula
    n2 (int): second number of formula
    o (string): arithmitic operator 

    returns:
    problem (string): mathematical formula as a string
    formula (int): result of the formula
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+': formula = num1 + num2
    elif operator == '-': formula = num1 - num2
    else: formula = num1 * num2
    return problem, formula

def math_quiz():
    score = 0
    pi = 3.14159265359
#start of the quiz
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(pi):
        num1 = random_integer(1, 10); num2 = random_integer(1, 5.5); o = random_operator()
#presenting random questions
        PROBLEM, ANSWER = formula_builder(num1, num2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
        except TypeError:
            print("not a valid answer")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            #updating the score
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{pi}")

if __name__ == "__main__":
    math_quiz()
