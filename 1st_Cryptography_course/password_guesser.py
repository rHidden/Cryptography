import itertools
import time
import string

def guess_password():
    with open("password.txt", "r") as password_file:
        password = password_file.readline().strip()

    start_time = time.time()
    tries = 0
    max_length = 10

    for length in range(1, max_length + 1):
        for guess in generate_guesses(length):
            tries += 1
            print(guess)
            if guess == password:
                end_time = time.time()
                time_taken = end_time - start_time
                print(f"Password found: {guess}")
                print(f"Tries: {tries}")
                print(f"Time taken: {time_taken:.2f} seconds")
                return

def generate_guesses(length):
    characters = string.printable
    for guess in itertools.product(characters, repeat=length):
        yield ''.join(guess)

guess_password()
