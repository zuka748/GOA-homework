import math
from turtle import*
def heart1(M):
    return 15*math.sin(M)**3

def heart2(M):
    return(12*math.cos(M)
           - 5*math.cos(2*M)
           - 2*math.cos(3*M)
           - math.cos (4*M))

speed (0.1)
bgcolor("black")

for i in range(0,600):
    goto(heart1(i) *18, heart2(i)*18)
    color ("dark red") 
    goto (0,0)

done()
    
