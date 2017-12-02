import random														#imports random
from guizero import App, Text, TextBox, Box, PushButton, Slider 	#imports guizero and guizero functions
global timesrolled 													#makes timesrolled a global function so that it will update with slide function calls
global sides 														#makes sides a global function so that it will update with button function calls
timesrolled=1 														#sets timesrolled to a minimum of 1, since it won't work with zero.
sides=4 															#probably should have set this to 6, but I feel 4 is more consistent with the interface.

def dfour():														#each button is assigned to a separate sided dice.  
	global sides													#reiterates that sides is a global function.  
	sides=4															#sets sides to 4
	print("Button was set to: " + str(sides))						# creates a history of setting sides in the terminal.
	return 0														#returns nothing
def dsix():
	global sides
	sides=6
	print("Button was set to: " + str(sides))
	return 0
def deight():
	global sides
	sides=8
	print("Button was set to: " + str(sides))
	return 0
def dten():
	global sides
	sides=10
	print("Button was set to: " + str(sides))
	return 0
def dtwelve():
	global sides
	sides=12
	print("Button was set to: " + str(sides))
	return 0
def dtwenty():
	global sides
	sides=20
	print("Button was set to: " + str(sides))
	return 0

def dcoin():														#creates a special define for coin tosses.
	sides=2															#limits sides to 2
	flip=random.randint(1,sides)									#creates a flip variable that uses the two sides.
	messagebox=Text(app, text="                              ", grid=[12,0])  #clears the location field of any pre-existing output in a dirty manner	
	if flip==1:														#checks to see if the flip number is 1												
		messagebox=Text(app, text="The flip is heads", grid=[12,0], color="magenta") #outputs text if the flip is 1 that the toss is heads.
	else:															#if the flip is not 1 (and is 2), then it outputs that text.
		messagebox=Text(app, text=" The flip is tails ", grid=[12,0], color="green") #output text if the flip is 2 that the toss is tails.
	print("1 is heads, 2 is tails and the result is: " +str(flip))  #creates a history of the event in the terminal.
	return 0
def dhondo():
	global sides
	sides=100
	print("Button was set to: " + str(sides))
	return 0

def rolldice():	#creates a rolling function.
	print("The type of dice chosen for this roll is: " +str(sides))	#creates a history of the event in the terminal.	
	print("The number of times to roll teh dice is: " +str(timesrolled)) #creates a history of the event in the terminal.
	newroll=int(timesrolled) #creating a local variable that is the int of timesrolled was probably not necessary.
	newsides=int(sides) #creatign a local variable that is the int of sides was probably not necessary.
	zombies=[] #establishes a blank list to store the roll results with a shout out to Steve Jackson games.
	cast=0  #sets the number of times cast to zero
	total=0 #sets the total sum of the dice to zero.
	while cast < newroll:	#creates a loop for rolling the dice as many times as the person has chosen with the slider.
         roll=random.randint(1,newsides) #sets the dice roll results between 1 and the number of sides on the appropriate dice.
         print ("The roll on the dice was: " + str(roll)) #creates a history of the event in the terminal
         zombies.append(roll) #adds the result to the list.
         total = total+roll #increases the total.
         cast=cast+1
	print("The total of the dice rolls was: " + str(total))	#creates a history of the event in the terminal
	#the following fields clear any existing text stored in the gui.  It's a dirty method.
	messagebox= Text(app,text="                                                                                                                                       ", grid=[7,0])
	messagebox= Text(app,text="                                                                                                                                       ", grid=[8,0])
	messagebox= Text(app,text="                                                                                                                                       ", grid=[9,0])
	messagebox= Text(app,text="                                                                                                                                       ", grid=[10,0])
	#the following outputs the results to the gui.
	messagebox= Text(app,text="The rolls are:", grid=[7,0], color="red")
	messagebox= Text(app,(zombies), grid=[8,0], color="green")
	messagebox= Text(app,text="The total is:", grid=[9,0], color="red")
	messagebox= Text(app,(total), grid=[10,0], color="blue")
	
	
def slider_changed(slider_value):	#this is the part that allows the timesrolled slider to be adjusted
	set(slider_value)				#this sets the slider value 
	global timesrolled				#this makes timesrolled global
	timesrolled=(slider_value)		#this sets the timesrolled condition to the slider value 
	
app = App(title="Dice App", height=600, width=900, layout="grid")	#creates the initial app box with a grid layout.
text = Text(app, text="Choose your dice", grid=[0,0])				#has the text to choose a dice type
box = Box(app, layout="grid", grid=[0,1])
button1 = PushButton(box, command=dfour, text="4", grid=[0,0])		#sets the locations for each button with the command related to each side
button2 = PushButton(box, command=dsix, text="6", grid=[0,1])
button3 = PushButton(box, command=deight, text="8", grid=[0,2])
button4 = PushButton(box, command=dten, text="10", grid=[1,0])
button5 = PushButton(box, command=dtwelve, text="12", grid=[1,1])
button6 = PushButton(box, command=dtwenty, text="20", grid=[1,2])
button8 =PushButton(box, command=dcoin, text="Coin", grid=[0,3])
button8 =PushButton(box, command=dhondo, text="100", grid=[1,3])
text2= Text(app, text="Choose # of rolls.", grid=[3,0])				#creates the text to choose the number of rolls next to the slider.
slider = Slider(app, command=slider_changed, start=1, end=20, grid=[2,1])
button9 =PushButton(box, command=rolldice, text="Roll", grid=[5,0])

app.display()