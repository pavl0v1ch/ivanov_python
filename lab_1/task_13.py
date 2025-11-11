import random

target = random.randint(1, 100)
guess = None

print("Попробуй угадать число от 1 до 100!")

while guess != target:
    guess = int(input("Введите число: "))

    if guess < target:
        print("Загаданное число больше.")
    elif guess > target:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляем! Вы угадали: {target}")