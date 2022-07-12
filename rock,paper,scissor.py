import random 

choices = ('r','p','s')
c_score = 0
p_score = 0

def player():
    
    ''' This fuction is used to get player choice. '''
    global choices
    symbol = input("choose either rock(r),paper(p),scissor(s).").lower()
    
    if symbol not in choices : 
        print(" You did not enter a valid option.")
        return player()
    else:
        return symbol
    
def computer():
    
    '''This function is used to get computers choice'''        
    return random.choice(choices)
        
def game():
    
    '''This function is used to play a single round of game'''
    global c_score, p_score
    p_choice = player()
    c_choice = computer()
    print("The computer has chosen : ",c_choice)
    print("you chose :",p_choice)
    if p_choice == c_choice:
        print("Its a tie and no one gets a point")
    elif (p_choice == "r" and c_choice == "s") or (p_choice == "s" and c_choice == "p") or (p_choice == "p" and c_choice == "r"):
        print("you won! ")
        p_score += 1
    else:
        print("aww i won.")
        c_score += 1
print("Welcome to rock,paper and scissor game!!!")
while True:
    for i in range(5):
        game()
    print("Good job!\nYour score is:", p_score, "\nComputer score is", c_score)
    print()
    again = int(input("press 1 to continue\npress 2 to reset and continue\npress 3 to exit the game\n"))
    if again == 1:
        continue
    elif again == 2:
        p_score = 0
        c_score = 0
        continue
    else:
        break

print("ok! Bye! 👋👋")