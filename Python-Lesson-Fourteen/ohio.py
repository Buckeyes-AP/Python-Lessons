from random import choice

capital = "Columbus"

bird = "Cardinal"

flower = "Red carnations"

song = "Hang on Sloopy"

def randomFunFact():
    funFacts = [
        "Ohio is known as the buckeye state.",
        "Seven U.S. presidents were born in Ohio.",
        "Columbus is the largest city in the state.",
        "Cincinnati reds is the first and oldest professional baseball team."
    ]
    
    index = choice("0123")
    
    print(funFacts[int(index)])
    
if __name__ == "__main__":
    randomFunFact()