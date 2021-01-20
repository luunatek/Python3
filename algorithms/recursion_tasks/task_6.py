"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random

def random_num_generator():
    random_num = random.randint(0, 100)

    user_input = int(input("Guess the number: "))

    if user_input != random_num and user_input < random_num:
        print("Entered number is too small, try again: ")

    elif user_input != random_num and user_input > random_num:
        print("Entered number is too small, try again: ")

    elif user_input == random_num:
        print(f"Congratulations, {user_input} is correct.")

random_num_generator()
