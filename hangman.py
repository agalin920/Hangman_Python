def hangman(word):
    wrong_guesses = 0   #Guess counter
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"] #Hangman body stages
    remaining_letters = list(word) #list of letters that are still available (not used)
    letter_board = ["__"] * len(word)
    win = False

    print('########__Hangman__########')

    while wrong_guesses < len(stages) - 1: #6 attempts
        print('\n')

        guess = input("Guess a letter: \n")

        if guess in remaining_letters:  #check if letter has been used before
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman("hangman")
