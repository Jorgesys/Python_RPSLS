#RSPLS
# 0 - Rock
# 1 - Spock
# 2 - Paper
# 3 - Lizard
# 4 - Scissors
import simplegui
import random

def name_to_number(name):
   if name == "Rock":
        return 0
   elif name == "Spock":
        return 1
   elif name == "Paper":
        return 2
   elif name == "Lizard":
        return 3
   elif name == "Scissors":    
        return 4
   else:
        return -1

def number_to_name(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Lizard"
    elif number == 4:
        return "Scissors"    
    else:
        return "Try Again!"    
    
def rpsls(player_choice): 
    print ""
    print "Player chooses " + str(player_choice)
    player_number = name_to_number(player_choice)  
    if(player_number == -1):
        print "Please, write the option correctly!"
        return
    comp_number  = random.randrange(0, 5)
    name_comp_choice = number_to_name(comp_number)
    print "Computer chooses " + name_comp_choice

    difference = (comp_number - player_number) % 5    

    if difference == 1 or difference == 2:
        print "Player wins!"
    elif difference == 3 or difference == 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"

frame = simplegui.create_frame("Guess the number:", 200, 200)
frame.add_input("Choose: Rock - Paper - Scissors - Lizard - Spock?", rpsls, 200)
frame.start()


