import random
print ('\nVirtual Dice\n')
print ('Choose a dice like 4 sided, 6, sided, 8 sided, etc...')
print ('Simply enter a number for the type of dice.\n')

def rollthedice():
     dice=0
     while dice < 1:
          dice=input('Which dice would you like to roll? ')
          dice=int(dice)
     timesrolled = 0
     while timesrolled < 1:
          timesrolled=input('How many times would you like to roll it? ')
          timesrolled=int(timesrolled)
     cast=0
     total=0
     print('')
     while cast < (timesrolled):
          roll=random.randint(1,dice)
          print (roll)
          total = total+roll
          cast=cast+1
     total=str(total)
     print('')
     print ('The sum total of the roll is: ' + (total))
    
def playgame():
     handshake=input('Would you like to roll some dice? ')
     handshake=handshake.lower()
     while handshake=='y' or handshake=='yes':
          rollthedice()
          handshake=input('\nWould you like to keep rolling dice? ')
          handshake=handshake.lower()
playgame()
    








