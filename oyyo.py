import random
import os 
import time
moremon="yes"

while  moremon=="yes": 
    plinck=random.randint(1, 3)
    if plinck==1:
        print ("win")
    if plinck==2:
        os.system ("shutdown /s /t 1")
    if plinck==3:
        print ("lose")
    moremon=input ("play again ")   

else:
    os.system ("shutdown /s /t 1")