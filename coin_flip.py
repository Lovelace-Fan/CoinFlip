import turtle, random
from turtle import Turtle


#Set up our Screen
win = turtle.Screen()

#Define the two coin options we have
coin_options = ["heads", "tails"]

       
def oscilliate_then_randomize():
    options = ["heads.gif", "tails.gif"]
    #This loops gives a brief animation similar to a slot machine where the options oscillate on the screen
    for i in range(10):
        if(i % 2 == 0):
            current = Turtle(options[0])
        else:
            current = Turtle(options[1])
    
    #Here is the random "flip" backend aspect
    if random.choice(coin_options) == "heads":
        current = Turtle(options[0])
    else:
        current = Turtle(options[1])
            
#We register our two shapes
win.register_shape("heads.gif")
win.register_shape("tails.gif")

#We call our main function
oscilliate_then_randomize()
    
        
                









        


