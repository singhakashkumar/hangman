import random

from hangman_art import stages
from hangman_art import logo
from hangman_wordlist import word_list

print("\n" + logo + "\n")

chosen_word = random.choice(word_list).lower()
result = list()
for letter in range(len(chosen_word)):
    result.append('_')
end_of_game = False

lives = 6

while (not end_of_game) and lives:
    guess = input("\nGuess a letter: ").lower()

    if guess in result:
      print("\nAlready guessed the character.\nTry another character.")
      continue


    for index in range(len(chosen_word)):
        if chosen_word[index] == guess :
            result[index]=guess
            present = True 
    if guess not in chosen_word:
        print("\nThe letter "+ guess + " not in the word. You lose a life\n")
        lives-=1


    print(result)
    print(stages[lives])
    if '_' not in result:
        end_of_game = True
        print('You won!')
    if lives == 0:
        end_of_game = True
        print("You lose.")
        print("The word is "+ chosen_word+".")
        
