from music_words import musicly_words
import random
from Hangman_Art import stages
from Hangman_Art import logo
from Sporty_words import Sport_words
from music_words import musicly_words
from Astronomy_words import Astronomy__words
names_list = ["Jamal", "Jarad", "Jamarion"]
Points = 0
saved_friends = 3

def check_friend():
    while True:
        print("The Hangman Boss has captured 3 of your friends. You must save them all.")
        print("It would help if you guessed the correct word hurry up because your friends are waiting for you.")
        friend_name = input("The 3 friends' names are Jarad, Jamal, and Jamarion. Who would you like to save first?\n")
        if friend_name in names_list:
            print(f"\n You have chosen to save {friend_name}. ")
            return friend_name
        else:
            print(f"\n {friend_name} is not present in the list.")

def play_for_friend(friend_name):
    if friend_name == 'Jarad':
        print('\n Jarad is a good choice. He is a very smart and intelligent boy. He is also a very good friend. You have saved Jarad. He is very interested in astronomy.')
        play_hangman(friend_name,Astronomy__words)
    if friend_name == 'Jamal':
        print('\n \n Jamal is a good choice, I mean, he is a bit dumb. He is also a very good friend. You have saved Jamal. He is very interested in sports, but he is bad at studies he loves football and Cricket. Make your guesses wisely')
        play_hangman(friend_name,Sport_words)
    if friend_name == 'Jamarion':
        print('\n Jamarion is a boy who closes himself from the outside world by literally listening to music almost 24/7, He is also a insecure person. You have saved Jamarion.')
        play_hangman(friend_name,Musicly_words)         

def play_hangman(friend_name,word_list):
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 6
    end_of_game = False


    print(logo)
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")


            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print("The word was " + chosen_word)

        print(f"{' '.join(display)}")

        if "_" not in display:
            global saved_friends
            global Points
            Points = Points + 1
            saved_friends = saved_friends -1
            print({saved_friends})

            print("You win.")
            print("Your points are " + str(Points))
            end_of_game = True

        print(stages[lives])


chances = 3
while chances > 0:
    friend_name = check_friend()
    play_for_friend(friend_name)
    chances -=1
print("\n\nThank You !")    

