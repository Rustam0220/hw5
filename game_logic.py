from decouple import config
import random

class CasinoGame:
    def __init__(self):
        self.money = int(config("MY_MONEY", default=1000))
        self.slots = list(range(1, 11))

    def start(self):
        while True:
            self.print_status()
            bet = self.get_bet()
            win_slot = random.choice(self.slots)
            if win_slot == bet:
                self.money += bet * 2
                print("Вы выиграли!")
            else:
                self.money -= bet
                print("Вы проиграли!")
            if self.money <= 0:
                print("У Вас закончились деньги. Игра окончена.")
                break
            play_again = input("Хотите сыграть еще? (да/нет): ")
            if play_again.lower() != "да":
                break

    def print_status(self):
        print(f"Ваш текущий капитал: {self.money}S")

    def get_bet(self):
        while True:
            try:
                bet = int(input("Введите ставку (от 1 до 10): "))
                if 1 <= bet <= 10:
                    return bet
                else:
                    print("Некорректная ставка. Попробуйте снова.")
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")

