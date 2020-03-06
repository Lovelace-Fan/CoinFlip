import turtle, random
from turtle import Turtle


win = turtle.Screen()
coin_options = ["heads", "tails"]

if random.choice(coin_options) == "heads":
    win.register_shape("heads.gif")
    heads = Turtle("heads.gif");
    
else:
    win.register_shape("tails.gif")
    tails = Turtle("tails.gif");
    
   
       
        
                









        


