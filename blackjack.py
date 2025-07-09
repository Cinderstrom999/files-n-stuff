
import random 
import time

def addCards(urhund):
    totalValue = 0
    for i in range(len(urhund)):
        hund=urhund[i].split(" ")
        try:
            hundy = int(hund [0])
        except:
            hundy = 10
        totalValue += hundy
    return totalValue

def checkWin(urhund, theyhund):
    print (":P")
    hunds= addCards(urhund)
    hundys=addCards(theyhund)
    if hunds>hundys:
        return True
    return False       


print(":D")
bellagio=[]
for i in range (10):
    for x in range (4):
        if i <= 8: 
            card= f"{i+2}"
            if x==0:
                card=card+" of lancers"
            elif x==1:
                card=card+" of berdly"
            elif x==2:
                card=card+ " of tenna"
            elif x==3:
                card=card+ " of ROARING NIGHT (pathetic) raaaaaaaaaaaaar"
            bellagio.append(card)
        else:
            neutrals=["lancer", "berdly","tenna"]
            for z in range (3): 
                if x==0:
                    card=neutrals[z]+" of lancers"
                elif x==1:
                  card=neutrals[z]+" of berdlys"
                elif x==2:
                   card=neutrals[z]+" of tennas"
                elif x==3:
                    card=neutrals[z]+" of ROARING NIGHT (pathetic) raaaaaaaaaaaaar"
                bellagio.append(card)
bellagio.append("joker")
print (bellagio)
bellagio.append("glass joker")


print (":D")
boodget=300
buget=99999999999999

while True:
    playerstate = True
    compstate = True
    playerhand=[]
    notsoAI=[]
    playedcards=[]

    card = bellagio[random.randint(0,49)]
    playerhand.append(card) 
    playedcards.append(card)
    print ("")
    print ("new reounD:")
    print ("you have ",boodget," 'insert dollar symbalo here'")
    cashdotpy=int(input("how much 'insert dollar symbal' u want back or lose "))

    while True:
      
        sec_card = bellagio[random.randint(0,49)]
        if sec_card in playedcards:
            continue 
        playerhand.append(sec_card) 
        playedcards.append(sec_card)
        break

    comp_card = bellagio[random.randint(0,49)]
    notsoAI.append(comp_card) 
    playedcards.append(comp_card)
    while True:
        sec_card = bellagio[random.randint(0,49)]
        if sec_card in playedcards:
            continue 
        notsoAI.append(sec_card) 
        playedcards.append(sec_card)
        break


    while True:
        print()
        print(playerhand)
        hundvalue = addCards(playerhand)
        notsoAIvalve= addCards(notsoAI)
        print("Player card value: ", hundvalue)
        
        if "glass joker" in playerhand:
            DX=random.randint(1,4)
            if DX==3:
                boodget-=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            else:
                boodget+=(100+cashdotpy)
                print ("U GOT GLASS JOKER u win also u wont get so luck next time (glass joker shattering sound)")
                break

        
        if  "joker" in playerhand:
            print ("congr]tasg[s [yiot]iuu w[ion]")
            boodget+=cashdotpy
            break
        if "joker" in notsoAI: 
            while True:
                print ("A{iII] win bu[gin] sour{seeeeeeeee) codde power [off]ing cgjhfs bvhjdxz")
        if hundvalue >21:
            print ("ur hund busted remeber kids 99% of gambelers win big U SUCK try agin")
            print("Computer card value: ", notsoAIvalve)
            boodget-=cashdotpy
            break
    
        if notsoAIvalve >21:
            print ("AI hund busted remeber kids 99% of gambelers win big and so do u")
            print("Computer card value: ", notsoAIvalve)
            boodget+=cashdotpy
            break
        if hundvalue==21:   
            print ("21 WOOOOOOO PARTY U WIN 20 WUUUUUUUUUUUN YAYAYYAYA")
            print("Computer card value: ", notsoAIvalve)
            boodget+=cashdotpy*2
            break
        if notsoAIvalve==21:
            print ("AI hund got 21 remeber kids 99% of gambelers win big U SUCK try agin")
            print("Computer card value: ", notsoAIvalve)
            boodget-=cashdotpy*2
            break
        if playerstate == False and compstate == False:
            if checkWin(playerhand, notsoAI):
                print ("u win :D play aing or the D:'s will come 4 u ")
                print("Computer card value: ", notsoAIvalve)
                boodget+=cashdotpy
                break
            print ("i think ul win next time |: playanig")
            print ("bonana eat mon mon gulp gulp yum!")
            print("Computer card value: 1 wait how is thatn even posible? idk i blame the maker of this lousey game :P")
            boodget-=cashdotpy/2
            break   

        if playerstate:
            playercose = input("more or all done ")
        
            if playercose== "more":
                while True:
                    new_card = bellagio[random.randint(0,49)]
                    if new_card in playedcards:
                        continue 
                    playerhand.append(new_card) 
                    playedcards.append(new_card)
                    break
            else:
                playerstate= False 
        
        if notsoAIvalve<=16:
            while True:
                poo_card = bellagio[random.randint(0,49)]
                if poo_card in playedcards:
                    continue 
                notsoAI.append(poo_card) 
                playedcards.append(poo_card)
                break
        else:
            compstate = False
        time.sleep(1)

