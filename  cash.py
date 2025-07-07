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
bank = 0
player1bank = 500
player2bank = 555
richboibank = 999

while True:
    if round==False:

        print ("player 1 turn XD")
        drac=bellagio[random.randint(0,48)]
        player1.append(drac)
        dracsplayed.append(drac)
        print("u drew "+drac + " sounds nice")
        if drac == "joker":
            print("congr]tasg[s [yiot]iuu w[ion]")
            player1bank+=bank
        elif drac == "oceans joker":
            print("u lose, remember kids 99.9999999999999% of gambelers quit befoere they win big!!!")
            richboibank+=bank
        



