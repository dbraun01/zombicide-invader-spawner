import numpy as np
import csv
import random

# variables
card_id = []
blue = []
yellow = []
orange = []
red = []

# Read input data
with open("Zombicide_ Invader-Spawns.csv") as csvfile:
   myfile = csv.reader(csvfile, delimiter=';', quotechar='"')
   for row in myfile:
      if row[0].isnumeric():
         card_id.append(row[0])
         blue.append(row[1] + ' ' + row[2])
         yellow.append(row[3] + ' ' + row[4])
         orange.append(row[5] + ' ' + row[6])
         red.append(row[7] + ' ' + row[8])

random.shuffle(card_id)

action = ''
last_action = ''
counter = 0
while action != 'exit':
   if counter >= len(card_id):
      print('All cards have been drawn: reshuffle.')
      counter = 0

   action = input()

   if action == '':
      action = last_action


   if action == 'shuffle':
      random.shuffle(card_id)
      counter = 0
   elif action == 'blue':
      print(blue[int(card_id[counter])-1])
      counter += 1
   elif action == 'yellow':
      print(yellow[int(card_id[counter])-1])
      counter += 1
   elif action == 'orange':
      print(orange[int(card_id[counter])-1])
      counter += 1
   elif action == 'red':
      print(red[int(card_id[counter])-1])
      counter += 1
   elif action == 'exit':
      print('Exit the program')
   elif action == 'save':
      with open('save.txt', 'w') as out:
         out.write(str(counter) + '\n')
         for i in card_id:
            out.write(str(i) + '\n')
   elif action == 'load':
      with open('save.txt', 'r') as saveFile:
         lines = saveFile.read().splitlines()
         first_row = True
         card_id = []
         for l in lines:
            # first row is counter
            if first_row:
               counter = int(l)
               first_row = False
            else:
               card_id.append(l)
   elif action == 'deck':
      print(str(counter) + '/' + str(len(card_id)))
   else:
      print('invalid entry')
      print('- shuffle: shuffle the card deck')
      print('- blue: draw a card at blue danger level')
      print('- yellow: draw a card at yellow danger level')
      print('- orange: draw a card at orange danger level')
      print('- red: draw a card at red danger level')
      print('- save: save the current session in the save file')
      print('- load: load the last saved session')
      print('- deck: indicate the number of cards drawn in the deck')
      print('- exit: exit the program')

   last_action = action
