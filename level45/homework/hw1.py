#1
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

#2
def rps(p1, p2):
    if p1==p2:
        return "Draw!"
    elif p1=="rock"and p2=="scissors":
        return "Player 1 won!"
    elif p1=="scissors"and p2=="paper":
        return "Player 1 won!"
    elif p1=="paper"and p2=="rock":
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    
#3
