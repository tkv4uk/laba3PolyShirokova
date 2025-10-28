import random


def rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]

    print("Игра 'ЦУ-Е-ФА'")
    print("Давай узнаем, кто сильнее!")
    print("Выбери: камень, ножницы или бумага")

    while True:
        user_choice = input("Твой выбор (или 'выход' для завершения): ").lower()

        if user_choice == "выход":
            print("Спасибо за игру! Возвращайся!")
            break

        if user_choice not in choices:
            print("Неверный выбор! Попробуй еще раз.")
            continue

        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice}")

        if user_choice == computer_choice:
            print("Ничья! Сыграем еще раз?")
        elif (user_choice == "камень" and computer_choice == "ножницы") or \
                (user_choice == "ножницы" and computer_choice == "бумага") or \
                (user_choice == "бумага" and computer_choice == "камень"):
            print("Поздравляю! Ты выиграл!")
        else:
            print("Увы, на этот раз ты проиграл!")


rock_paper_scissors()