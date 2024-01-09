import random
import time

def play_game():
    number = random.randint(1, 500)
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'")
    print("Попробуйте угадать число от 1 до 500")

    while True:
        guess = int(input("Введите вашу догадку (для выхода напишите 0) >> "))
        attempts += 1
    
        if guess == 0:
            print("Игра завершена!")
            break
        elif guess < number:
            print("Загаданное число больше вашей догадки")
        elif guess > number:
            print("Загаданное число меньше вашей догадки")
        else:
            print("Поздравляю, вы угадали число!")
            break

    print(f"Вы угадали число за {attempts} попыток, спасибо за игру!")
