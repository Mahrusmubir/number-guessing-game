from abc import ABC, abstractmethod
import random

class GuessGame(ABC):
    @abstractmethod
    def welcome_message(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass

    @abstractmethod
    def check_input(self, user_input):
        pass

    @abstractmethod
    def generate_random_number(self, top_range):
        pass

    @abstractmethod
    def compare_numbers(self, user_number, random_number):
        pass

    @abstractmethod
    def print_result(self, attempts):
        pass

    def play_game(self):
        self.welcome_message()
        user_input = self.get_user_input()
        if not self.check_input(user_input):
            print("Invalid input. Quitting the game.")
            return

        top_range = int(user_input)
        if top_range < 0:
            print("The top range cannot be negative. Quitting the game.")
            return

        random_number = self.generate_random_number(top_range)
        attempts = 0

        while True:
            user_number = int(input("Enter your guess: "))
            attempts += 1

            if self.compare_numbers(user_number, random_number) == 0:
                self.print_result(attempts)
                break

    def run(self):
        self.play_game()

class ConcreteGuessGame(GuessGame):
    def welcome_message(self):
        print("Welcome to the Guessing Game!")

    def get_user_input(self):
        return input("Enter the highest number for the guessing range: ")

    def check_input(self, user_input):
        return user_input.isdigit()

    def generate_random_number(self, top_range):
        return random.randint(1, top_range)

    def compare_numbers(self, user_number, random_number):
        if user_number > random_number:
            print("Your guess is too high!")
        elif user_number < random_number:
            print("Your guess is too low!")
        else:
            return 0

    def print_result(self, attempts):
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

game = ConcreteGuessGame()
game.run()
