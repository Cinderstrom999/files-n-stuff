import random 

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


round = False
dracsplayed=[]
player1 = []
player2 = []
bank1 = 0
bank2 = 0
player1bank = 500
player2bank = 555
richboibank = 999

print ("new round")
print ("player 1 turn XD")
bank1=int(input("how much $$$"))
drac=bellagio[random.randint(0,49)]
player1.append(drac)
dracsplayed.append(drac)

while True:
    ndrac = bellagio[random.randint(0,49)]
    if ndrac in dracsplayed:
        continue
    player1.append(ndrac)
    dracsplayed.append(ndrac)
    break

print(player1)
if "joker" in player1:
    print("congr]tasg[s [yiot]iuu w[ion]")
    player1bank+=bank1
    richboibank-=bank1 

elif "oceans joker" in player1:
    print("u lose, remember kids 99.9999999999999% of gambelers quit befoere they win big!!!")
    richboibank+=bank1
    player1bank-=bank1

print ("player 2 turn XD")
bank2=int(input("how much $$$"))
drac=bellagio[random.randint(0,49)]
player2.append(drac)
dracsplayed.append(drac)

while True:
    ndrac = bellagio[random.randint(0,49)]
    if ndrac in dracsplayed:
       continue
    player2.append(ndrac)
    dracsplayed.append(ndrac)
    break

print("u drew "+drac + " sounds nice")
if "joker" in player2:
    print("congr]tasg[s [yiot]iuu w[ion]")
    player2bank+=bank2
    richboibank-=bank2 
    
elif "oceans joker" in player2:
    print("u lose, remember kids 99.9999999999999% of gambelers quit befoere they win big!!!")
    richboibank+=bank2
    player2bank-=bank2
            
elif bank2=="m5n4b3v2cx1":
    print ("welcome agent i hope the trip was nice,i know the meeting site could crash at any molment but, when it strikes 22:22:22 your time is up good luck agent homes good luck")
    print (time.ctime(time.time()+10800))
    time.sleep(1)

    
        



