#Tymoteusz Maj
#Github: Xeraoo
#Zadanie 9


import random

class GuessingGame:
    def __init__(self, max_number=10):
        self.max_number = max_number  # maksymalna liczba, jaką gracz może wybrać
        self.secret_number = random.randint(1, max_number)  # wybierana losowo tajna liczba
        self.num_guesses = 0  # licznik prób

    def __repr__(self):
        return f"Gra w zgadywanie liczb (max_number={self.max_number}, secret_number={self.secret_number}, num_guesses={self.num_guesses})"

    def __str__(self):
        return f"Myślę o liczbie z zakresu od 1 do {self.max_number}."

    def __len__(self):
        return self.num_guesses  # zwraca liczbę prób, jakie gracz podjął

    def __eq__(self, other):
        return self.secret_number == other.secret_number  # zwraca True, jeśli obiekt innej gry ma taką samą tajną liczbę

    def guess(self, number):
        self.num_guesses += 1  # zwiększa licznik prób
        if number == self.secret_number:
            print(f"Zgadłeś! Prawidłowa odpowiedź to: {self.secret_number}. Udało ci się to w {self.num_guesses} próbach.")
            return True  # zwraca True, jeśli gracz odgadł liczbę
        elif number < self.secret_number:
            print("Podaj wyższą wartość!")
            return False  # zwraca False, jeśli liczba gracza jest mniejsza niż tajna liczba
        else:
            print("Podaj niższą wartość!")
            return False  # zwraca False, jeśli liczba gracza jest większa niż tajna liczba


game = GuessingGame(max_number=10)  # tworzy nową grę z maksymalną liczbą 10
print(game)  # wyświetla informację o zakresie liczb

while True:
    try:
        guess = int(input("Podaj liczbę: "))  # prosi gracza o podanie liczby
        if game.guess(guess):  # wywołuje metodę guess i przerywa pętlę, jeśli gracz odgadł liczbę
            break
    except ValueError:
        print("Podaj poprawną wartość.")  # wyświetla komunikat o błędzie, jeśli gracz podał nieprawidłowy typ

print(f"Gra zakończona! Zajęło ci to {len(game)} prób.")  # wyświetla liczbę prób, jakie gracz podjął w trakcie gry

