import random
print ('\nExploding Dice\n')
print ('Choose a dice like 4 sided, 6, sided, 8 sided, etc...')
print ('Simply enter a number for the type of dice.\n')

def rollthedice():
     dice=0
     while dice < 1:
          dice=input('Which dice would you like to roll? ')
          dice=int(dice)
     timesrolled = 1
     cast=0
     total=0
     explode=0
     fail=0
     print('')
     while cast < (timesrolled):
          roll=random.randint(1,dice)
          print (roll)
          if roll==dice:
          	  print('Boom!')	  
          	  cast=cast-1
          	  fail=fail+1
          total = total+roll
          cast=cast+1
     total=str(total)
     print('')
     print ('The sum total of the roll is: ' + (total))
     if roll==1 and fail is 0:
     	 print('This was a failure!')
     	 explode=1
     wildtimes=1
     ace=6
     wildcast=0
     wildtotal=0
     wildice=0
     while wildcast < (wildtimes):
     	 	wildroll=random.randint(1,ace)
     	 	print (wildroll)
     	 	if wildroll==ace:
     	 		print('Ace!')
     	 		wildcast=wildcast-1
     	 	wildtotal= wildtotal + wildroll
     	 	wildcast=wildcast + 1
     print('The sum total of the wild die is: ' + str(wildtotal))
     if wildroll==1 and explode==1:
     	 print('CRITICAL FAILURE!!!')
def acing():
	print('Exploding!!!!')
	roll=random.randint(1,dice)
	print (roll)
	total = total+roll

def playgame():
     handshake=input('Would you like to roll some dice? ')
     handshake=handshake.lower()
     while handshake=='y' or handshake=='yes':
          rollthedice()
          handshake=input('\nWould you like to keep rolling dice? ')
          handshake=handshake.lower()
playgame()
    








