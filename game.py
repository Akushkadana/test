import random


def check_guess(secret_number, guess):
    if guess == secret_number:
        return "WIN"
    elif guess < secret_number:
        return "LOW"
    else:
        return "HIGH"


def run_test_game():
    secret_number = random.randint(1, 100)
    max_attempts = 10

    print("Компьютер загадал число от 1 до 100.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Попытка {attempt}. Введите число: "))
        except ValueError:
            print("Ошибка! Введите целое число.")
            continue

        result = check_guess(secret_number, guess)

        if result == "WIN":
            print("ПОБЕДА!")
            return

        elif result == "LOW":
            print("Загаданное число БОЛЬШЕ.")

        else:
            print("Загаданное число МЕНЬШЕ.")

    print("ПРОИГРЫШ!")
    print("Загаданное число:", secret_number)


if __name__ == "__main__":
    run_test_game()