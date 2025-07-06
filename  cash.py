
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
bellagio.append("instint win WOW great job thats almost a 2% chance good job")
print (bellagio)

round = False
while True:
    player1 = []
    player2 = []
    

