import random

def run_test_game():
    secret_number = random.randint(1, 100)
    max_attempts = 10
    
    print(f"--- НАЧАЛО ТЕСТОВОЙ ИГРЫ (Макс. ходов: {max_attempts}) ---")
    print("Компьютер загадал число от 1 до 100.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Ход {attempt}/{max_attempts}. Введите число: "))
        except ValueError:
            print("Ошибка ввода! Введите целое число.")
            continue

        if guess == secret_number:
            print(f"ПОБЕДА! Вы угадали число {secret_number} за {attempt} ходов.")
            return {"result": "WIN", "attempts": attempt}
        elif guess < secret_number:
            print("Загаданное число БОЛЬШЕ.")
        else:
            print("Загаданное число МЕНЬШЕ.")

    print(f"ПРОИГРЫШ! Попытки закончились. Загаданное число было: {secret_number}")
    return {"result": "LOSE", "attempts": max_attempts}

if __name__ == "__main__":
    run_test_game()