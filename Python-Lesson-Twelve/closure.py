# Closure is a function having access to the scope of its parent 
# function after the parent function has returned.

def parentFunction(person, coins):
    # coins = 3
    
    def playGame():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        else:
            print("\n" + person + " is out of coins.")
            
    return playGame

tommy = parentFunction("Tommy", 3)
jenny = parentFunction("Jenny", 5)

tommy()
tommy()

jenny()

tommy()
