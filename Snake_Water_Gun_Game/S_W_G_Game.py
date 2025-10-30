import random

def game(Computer, You):
    if(Computer == You):
        return None
    elif (Computer == 's'):
        if (You == 'w'):
            return False
        elif (You == 'g'):
            return True
    elif (Computer == 'w'):
        if (You == 's'):
            return True
        elif(You == 'g'):
            return False
    elif(Computer == 'g'):
        if (You == 's'):
            return False
        elif(You == 'w'):
            return True                           
           
print("Copmuter's Turn: Snake(s), Water(w), Gun(g)")
randNo = random.randint(1, 3)
if(randNo == 1):
    Computer = 's'
elif(randNo == 2):
    Computer = 'w'
elif(randNo == 3):
    Computer = 'g'  

You = input("Your Turn: Snake(s), Water(w), Gun(g):\n") 
Score = game(Computer, You)


print(f"You choose {You}")
print(f"Computer chooses {Computer}")          

if (Score == None):
    print("It's a tie!")
elif(Score == False):
    print("You Lose..")
else:
    print("You Win") 