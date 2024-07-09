import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_number(player_name):
    while True:
        number = input(f"{player_name}, please set a multi-digit number: ")
        if number.isdigit() and len(number) > 1:
            return number
        print("Invalid input. Please enter a multi-digit number.")

def get_guess(player_name, num_length):
    while True:
        guess = input(f"{player_name}, enter your guess ({num_length} digits): ")
        if guess.isdigit() and len(guess) == num_length:
            return guess
        print(f"Invalid input. Please enter a {num_length}-digit number.")

def provide_hints(secret, guess):
    exact_matches = [s == g for s, g in zip(secret, guess)]
    correct_positions = [i + 1 for i, match in enumerate(exact_matches) if match]
    incorrect_positions = [i + 1 for i, match in enumerate(exact_matches) if not match]
    
    partial_matches = 0
    for g in guess:
        if g in secret and guess.count(g) <= secret.count(g):
            partial_matches += 1
    partial_matches -= sum(exact_matches)
    
    return correct_positions, incorrect_positions, partial_matches

def play_round(guesser_name, setter_name, secret):
    attempts = 0
    num_length = len(secret)
    while True:
        attempts += 1
        guess = get_guess(guesser_name, num_length)
        if guess == secret:
            print(f"{guesser_name} guessed the number {guess} correctly in {attempts} attempts!")
            return attempts
        correct_positions, incorrect_positions, partial_matches = provide_hints(secret, guess)
        print(f"Correct positions: {correct_positions}")
        print(f"Incorrect positions: {incorrect_positions}")
        print(f"Digits correct but in wrong positions: {partial_matches}")
        

def mastermind_game():
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")

    clear_screen()
    print(f"{player1}'s turn to set the number.")
    number1 = get_number(player1)
    clear_screen()
    print(f"{player2}'s turn to guess.")
    print(f"The number set by {player1} has {len(number1)} digits.")
    attempts_player2 = play_round(player2, player1, number1)

    clear_screen()
    print(f"{player2}'s turn to set the number.")
    number2 = get_number(player2)
    clear_screen()
    print(f"{player1}'s turn to guess.")
    print(f"The number set by {player2} has {len(number2)} digits.")
    attempts_player1 = play_round(player1, player2, number2)

    clear_screen()
    print(f"{player1} took {attempts_player1} attempts to guess the number.")
    print(f"{player2} took {attempts_player2} attempts to guess the number.")
    if attempts_player1 < attempts_player2:
        print(f"{player1} wins and is crowned Mastermind with {attempts_player1} attempts!")
    elif attempts_player1 > attempts_player2:
        print(f"{player2} wins and is crowned Mastermind with {attempts_player2} attempts!")
    else:
        print("It's a tie! Both players took the same number of attempts.")

if __name__ == "__main__":
    mastermind_game()
