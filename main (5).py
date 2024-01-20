
import random

from Astronomy_words import Astronomy__words
from Hangman_Art import logo
from music_words import Musicly_words
from Sporty_words import Sport_words
global wordlength
wordlength = 0

names_list = ["Jarad", "Jamal", "Jamarion"]
points = 0
UNSaved_friends = 3

def check_friend():
    while True:
        print("The Hangman Boss has captured 3 of your friends. You must save them all.")
        print("It would help if you guessed the correct word hurry up because your friends are waiting for you.")
        friend_name = input("The 3 friends' names are Jarad, Jamal, and Jamarion. Who would you like to save first?\n")
        if friend_name in names_list:
            print(f"\n You have chosen to save {friend_name}.")
            play_for_friend(friend_name)
            break
        else:
            print(f"\n {friend_name} is not present in the list.")
         


def play_for_friend(friend_name): 
  
  
   if friend_name == 'Jarad':
       print('\n Jarad is a good choice. He is a very smart and intelligent boy. He is also a very good friend. You have saved Jarad. He is very interested in astronomy. ')
       play_hangman(Astronomy__words)   
   if friend_name == 'Jamal':
       print('\n Jamal is a good choice, I mean, he is a bit dumb. He is also a very good friend. You have saved Jamal. He is very interested in sports, but he is bad at studies he loves football and Cricket.')
       play_hangman(Sport_words)
   if friend_name == 'Jamarion':
       print('\n Jamarion is a boy who closes himself from the outside world by literally listening to music almost 24/7, He is also a insecure person. You have saved Jamarion.')     
       play_hangman(Musicly_words)     
      

def play_hangman(word_list):
  global wordlength
  chosen_word = random.choice(word_list)
  wordlength = len(chosen_word) 
  



check_friend()
print(logo)
display = []
for _ in range(wordlength):
    display += "_"
