
#Importing Required Files
from replit import clear
import random
import ascii_art
print (ascii_art.logo + "\n")

#Randomly generating word
from world_list import word_list
word= random.choice(word_list)
value = [ ]

#Creating Staring conditions
for dash in range(len(word)):
  value = value + ['_']
lives= 6
start_game = True
user_guesses=[]


#Starting Game
while start_game:
  print(value)
  user_guess = input("Guess a letter: ").lower()
  clear()
  print(ascii_art.logo)
  if user_guess in user_guesses:
    print(f"\nYou have already guessed the letter '{user_guess}'")
  if user_guess not in list(word):
    print(f"\nThe letter '{user_guess}' is not in the word")
  counter=0
  if user_guess not in list(word):
    lives-=1
  for character in word:
    if character == user_guess:
      value[counter]=user_guess
    counter+=1
  print(ascii_art.stages[lives])
  if lives == 0:
    print ("You Lose!\nThe word is " + word)
    break
  if '_' in value:
    start_game = True
  else:
    start_game = False
    print ('You won!')
    print(f"{' '.join(value)}")
  user_guesses+=user_guess
