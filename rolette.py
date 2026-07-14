import random
import os
import time
import random
import webbrowser
import signal
import playsound3 


while True:
    rolte=random.randint (-1, 36)
    (guess)=input("bets for more info goto this link! https://en.wikipedia.org/wiki/Roulette press start again to open it                            ")
    time.sleep (5)
    os.system ("start chrome --new-window \"https://en.wikipedia.org/wiki/Roulette\" ")


    rolte1=random.randint (0,1)
    if rolte1==0:
        print ("black")
    else:
        print ("red")
    print (rolte)
    print ("heres your bet!", guess )
    (guess1)=input("plese tell money amount / loss if loss just put negigtive            ")
    bank=0
    
    if guess==(1, 999):
        bank+=guess1