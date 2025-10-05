import random


class FruitQuiz:
    def __init__(self):
        self.fruits = {'apple': 'red',
                       'banana': 'yellow',
                       'grape': 'purple'}

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))

            print(f"What is the color of {fruit}?")
            user_answer = input().strip()

            if user_answer.lower() == color:
                print("Correct!")
            else:
                print(f"Wrong answer — the color is {color}.")

            try:
                option = int(input("Enter 0 to play again, or 1 to stop: "))
            except ValueError:
                option = 1

            if option:
                break


print("Welcome to fruit color quiz")
fq = FruitQuiz()
fq.quiz()