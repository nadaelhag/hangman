# Homework (1+2), hangman.py
# Name: Nada Elhag/ Sarah Adawi
# Time spent:

# Hangman Game
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    infile = open(WORDLIST_FILENAME, 'r')
    line = infile.readline()
    wordlist_in = line.split()
    print(len(wordlist_in), "words loaded.")
    return wordlist_in


def choose_word(wordlist_in):
    return random.choice(wordlist_in)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    count = 0
    for i in secret_word:
        if i in letters_guessed:
            count += 1
    if count == len(secret_word):
        return True
    return False


def get_guessed_word(secret_word, letters_guessed):
    word = ""
    for j in secret_word:
        if j in letters_guessed:
            word += j
        else:
            word += " _ "
    return word


def get_available_letters(letters_guessed):
    word1 = string.ascii_lowercase
    if not letters_guessed:
        return word1
    word2 = ""
    for k in word1:
        if k not in letters_guessed:
            word2 += k
    return word2


def is_unique(secret_word):
    unique = set(secret_word)
    return len(unique)


def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    wrong_guesses = 0
    count_guess = 6
    warning = 3
    total_score = 0
    print(f"You have {warning} warnings left.")
    letters_guessed = []
    while count_guess > 0:
        print("--------------")
        print(f"You have {count_guess} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = str.lower(input("Please guess a letter: "))
        vowels = ["u", "a", "e", "i", "o"]
        if not guess.isalpha() or guess in letters_guessed:
            warning -= 1
            if warning < 0:
                warning = 0
                count_guess -= 1
                wrong_guesses += 1
            if not guess.isalpha():
                print(f"Oops! That is not a valid letter. You have {warning} warnings left: "
                      + get_guessed_word(secret_word, letters_guessed))
            if guess in letters_guessed:
                print(f"Oops! You've already guessed that letter. You now have {warning} warnings: "
                      + get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            if is_word_guessed(secret_word, letters_guessed):
                if warning == 3 and wrong_guesses == 0:
                    total_score = count_guess * is_unique(secret_word) + 3
                elif warning >= 0 and wrong_guesses > 0:
                    total_score = count_guess * is_unique(secret_word) + 1
                elif warning >= 0 or wrong_guesses > 0:
                    total_score = count_guess * is_unique(secret_word) + 2
                print("--------------")
                print("Congratulations, you won!")
                return (total_score / ((count_guess * is_unique(secret_word)) + 3)) * 10
        else:
            count_guess -= 1
            wrong_guesses += 1
            letters_guessed.append(guess)
            if guess in vowels:
                count_guess -= 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
    print("--------------")
    print("Sorry, you ran out of guesses. The word was " + secret_word)
    return 0


def match_with_gaps(my_word, other_word):
    joined = "".join(my_word.split())
    if len(joined) != len(other_word):
        return False
    emp = ""
    for z in range(len(joined)):
        # loop through indices and not letters!!
        if joined[z] != "_":
            if joined[z] != other_word[z]:
                return False
            emp += other_word[z]
        else:
            if other_word[z] in emp:
                return False
    return True


def show_possible_matches(my_word):
    matches = []
    for x in wordlist:
        if match_with_gaps(my_word, x):
            matches.append(x)
            print(x, end=" ")
    if len(matches) != 0:
        print()
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    wrong_guesses = 0
    count_guess = 6
    warning = 3
    print(f"You have {warning} warnings left.")
    total_score = 0
    letters_guessed = []
    while count_guess > 0:
        print("--------------")
        print(f"You have {count_guess} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = str.lower(input("Please guess a letter: "))
        vowels = ["u", "a", "e", "i", "o"]
        if not guess.isalpha() or guess in letters_guessed:
            if guess == "*":
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            else:
                warning -= 1
                if warning < 0:
                    warning = 0
                    count_guess -= 1
                    wrong_guesses += 1
                if not guess.isalpha():
                    print(f"Oops! That is not a valid letter. You have {warning} warnings left: "
                          + get_guessed_word(secret_word, letters_guessed))
                if guess in letters_guessed:
                    print(f"Oops! You've already guessed that letter. You now have {warning} warnings: "
                          + get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            if is_word_guessed(secret_word, letters_guessed):
                if warning == 3 and wrong_guesses == 0:
                    total_score = count_guess * is_unique(secret_word) + 3
                elif warning >= 0 and wrong_guesses > 0:
                    total_score = count_guess * is_unique(secret_word) + 1
                elif warning >= 0 or wrong_guesses > 0:
                    total_score = count_guess * is_unique(secret_word) + 2
                print("--------------")
                print("Congratulations, you won!")
                return (total_score / ((count_guess * is_unique(secret_word)) + 3)) * 10
        else:
            count_guess -= 1
            wrong_guesses += 1
            letters_guessed.append(guess)
            if guess in vowels:
                count_guess -= 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
    print("--------------")
    print("Sorry, you ran out of guesses. The word was " + secret_word)
    return 0


def choose_mode():
    mode = str.lower(input("Enter easy for easy mode or hard for hard mode: "))
    if mode == "hard":
        word = choose_word(wordlist)
        while not(len(word) > 5 and len(word) == len(set(word))):
            word = choose_word(wordlist)
        return word
    elif mode == "easy":
        word = choose_word(wordlist)
        while not(len(word) <= 5):
            word = choose_word(wordlist)
        return word
    else:
        print("Invalid input")


def play_game():
    print()
    print("Would you like to play with modes or without?")
    print("Enter 1 for modes")
    print("Enter 2 for no modes")
    answer = int(input())
    print("--------------")
    if answer == 1:
        secret_word_out = choose_mode()
        print("--------------")
        print("Would you like to play with or without hints?")
        print("Enter 1 for hints")
        print("Enter 2 for no hints")
        answer1 = int(input())
        print("-----------------------------------------------")
        if answer1 == 1:
            score = hangman_with_hints(secret_word_out)
            return score
        elif answer1 == 2:
            score = hangman(secret_word_out)
            return score
    elif answer == 2:
        secret_word_out = choose_word(wordlist)
        print("Would you like to play with or without hints?")
        print("Enter 1 for hints")
        print("Enter 2 for no hints")
        answer2 = int(input())
        print("-----------------------------------------------")
        if answer2 == 1:
            score = hangman_with_hints(secret_word_out)
            return score
        elif answer2 == 2:
            score = hangman(secret_word_out)
            return score


if __name__ == "__main__":
    option = "yes"
    n = 0
    score1 = 0
    while option != str.lower("no") and option != str.lower("Invalid input"):
        score_game = play_game()
        n += 1
        # if player has points, remove 1 from score for not guessing the word
        if score_game == 0 and score1 >= 1:
            score1 -= 1
        score1 = round((score1 + score_game) // n, 2)
        score2 = round(score_game, 2)
        print(f"Your score for this round is {score2} out of 10")
        option = str.lower(input("Would you like to play again? Please enter yes or no "))
        if option != "yes" and option != "no":
            option = "Invalid input"
            print("Invalid input")
            break
    print("--------------")
    print(f"Thank you for playing hangman! Your final score is {score1} out of 10")