
import random
from Hangman_Art import stages
from Hangman_Art import logo
from Astronomy_words import Astronomy__words
from music_words import Musicly_words

names_list = ["Jarad", "Jamal", "Jamerion"]
points = 0
UNSaved_friends = 3

def check_friend():
    while True:
        print("The Hangman Boss has captured 3 of your friends. You must save them all before the Hangman Boss can get them.")
        print("It would help if you guessed the correct word hurry up because your friends are waiting for you.")
        friend_name = input("The 3 friends' names are Jarad, Jamal, and Jamerion. Who would you like to save first?\n")
        if friend_name in names_list:
            print(f"\n You have chosen to save {friend_name}.")
            return friend_name
        else:
            print(f"\n {friend_name} is not present in the list.")
         

def play_for_friend(friend_name): 
  
  
   if friend_name == 'Jarad':
       print('\n Jarad is a good choice. He is a very smart and intelligent boy. He is also a very good friend. You have saved Jarad. He is very interested in astronomy. ')
   if friend_name == 'Jamal':
       print('\n Jamal is a good choice, I mean, he is a bit dumb. He is also a very good friend. You have saved Jamal. He is very interested in sports, but he is bad at studies he loves football and Cricket.')
   if friend_name == 'Jamerion':
       print('\n Jamerion is a boy who closes himself from the outside world by literally listening to music for 24 hours straight, He is also a insecure person. You have saved Jamerion.')     

chosen_friend = check_friend()
play_for_friend(chosen_friend)