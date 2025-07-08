
import random 

def addCards(urhund):
    totalValue = 0
    for i in range (len(urhund)):
        hund=urhund[i].split(" ")
        try:
            hundy = int(hund [0])
        except:
            hundy = 10
        totalValue += hundy
        return totalValue


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
bellagio.append("oceans joker")




print (":l")

playerhand=[]
notsoAI=[]
playedcards=[]






card = bellagio[random.randint(0,49)]
playerhand.append(card) 
playedcards.append(card)
while True:
    sec_card = bellagio[random.randint(0,49)]
    if sec_card in playedcards:
        continue 
    playerhand.append(sec_card) 
    playedcards.append(sec_card)
    break
print ("breadO:")
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
print ("breadO:")

playerstate = True
compstate = True
while True:
    hundvalue = addCards(playerhand)
    notsoAIvalve= addCards(notsoAI)
    if hundvalue >21:
        print ("ur hund busted remeber kids 99% of gambelers win big U SUCK try agin")
        break
    if notsoAIvalve >21:
        print ("AI hund busted remeber kids 99% of gambelers win big and so do u")
        break
    if hundvalue==21:   
        print ("21 WOOOOOOO PARTY U WIN 20 WUUUUUUUUUUUN YAYAYYAYA")
        break
    if notsoAIvalve==21:
        print ("AI hund got 21 remeber kids 99% of gambelers win big U SUCK try agin")
        break
    playercose = input("more or all done")
    if playercose== "more":
        while True:
            new_card = bellagio[random.randint(0,49)]
            if new_card in playedcards:
                continue 
            playerhand.append(sec_card) 
            playedcards.append(sec_card)
            break
    else:
        playerstate= False
    
    
    if notsoAIvalve<=16:
        

