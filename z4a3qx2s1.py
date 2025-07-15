import os 

import time 
import random 




runstart=input("hi this is billy shears the 7 year olds first project i hope yoh like it by the way what is your name? ")

if runstart=="mike oscar":
    while True:
        rpdoor=input("ah [sigh] i see well protocall active. rock paper sissors go ")
        door=random.randint (1,4)
        if door==(1) and rpdoor==("paper"):
            print ("nice, now go again, also do it better this time!!!")
        if door==(2) and rpdoor==("scissors"):
            print ("zxgzsdzdzxfasternexttimehasrvnpasdbpa")
        if door==(3) and rpdoor==("rock"):
            print ("you lose go agin")
        else:
            print ("toe")
    

if runstart==":D the :|":
    print (":D :| :] :( ) =D D= {=!!! =V")
    time.sleep(5)
    while True:
        print ("1q 2a 3z")
        print ("i win ")
        print("HOLWOW HEART")

if runstart=="big boi":
    print ("ok type this https://www.google.com/search?q=depth+first+search+solution&sca_esv=05f7f9216b2ed83f&ei=Fgh1aNraPNPsptQPvqbHoAQ&oq=depth+first+search+soultio&gs_lp=Egxnd3Mtd2l6LXNlcnAiGmRlcHRoIGZpcnN0IHNlYXJjaCBzb3VsdGlvKgIIADIGEAAYFhgeMgYQABgWGB4yCBAAGAgYDRgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiiBBiJBUikV1DQBFjPSHABeAGQAQCYAVGgAZEEqgEBOLgBAcgBAPgBAZgCCaACugTCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICChAAGIAEGEMYigXCAgUQABiABMICCxAAGIAEGJECGIoFwgIFECEYoAGYAwCIBgGQBgqSBwE5oAfYMbIHATi4B7cEwgcFMC41LjTIBx8&sclient=gws-wiz-serp")


if runstart=="ship":
    rig=input("1 ore 2 ")
    if rig=="1":
        print ("2 bad it 2")
    else:
        print ("2 bad it was 1")
    

if runstart=="idk hoew":
    print(" big   small blank")
    print(" small blank blank")
    print ("big   blank blank yay done")

if runstart=="line":
    print ("here line |")
    print ("          |")

if runstart=="meme":
    has=random.randint (1, 2)
    if has== (1):
        print ("lose")
        os.system("shutdown /s /t 1")
    if has== (2):
        print ("win oh no i fell on the power doen button")
        os.system ("shutdown /s /t 1")


if runstart=="jack black":
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
    chasebankdebt = False

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

        if chasebankdebt:
            if boodget>=100000:
                print("close call dont try us angin hahhahahahahhahahahahahahahahahahahahahahahahtakesbreathhahahahahahahahahahhahaahahahahahahahhahahahahahahahahahahahahahahaha")
                boodget-=100000
            else:
                while True:
                    print ("U R NOW KIDNAPPED HOPE U HAVE FUN WITH THE REST OF THEM")

        if boodget==69:
            print("wow real slick")

    
        if boodget<=-1000:
            print ("bank of saba wants its dollor sign back make 100000dollars in 1 trun or else")
            print ("- afsonso saba")
            chasebankdebt = True
        print ("you have ",boodget," 'insert dollar symbalo here'")
        cashdotpy=int(input("how much 'insert dollar symbal' u want back or lose also if you get -10000 banl< of sabas goons come 4 u "))

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
                    os.system ("shutdown /s /t 1")
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
        if cashdotpy=="jpeg":
            print ("hello graham your portal is waiting tank you. you know how to lye so w3ll hmm? yes the code is a bit ddddddddddddddddddddddddddddddooowwwnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn2n2n3nn64wzn, get in the car graham")


else:
    print ("oh hi " +runstart + " wellcome! yes i can take prior knowlege imprest family ha ha!!! Orange is a color and it’s cool. I like orange because it's not blue or green. Also, orange is like the sun, sometimes. That makes it bright and happy. People eat oranges too and they are orange, which is fun. Another reason orange is cool is because pumpkins. Pumpkins are orange and they are used on Halloween. Halloween is when people wear costumes. Orange is also on traffic cones. Traffic cones tell cars where to go and that’s kind of important probably. Orange clothes are also a thing. Some people wear them and look very orange. If you wear all orange you look like a carrot. That’s funny. Sometimes orange is too bright but it’s still fine. It's just the best I guess. So orange is very cool and not boring. If you don’t like orange that’s okay but you should. It’s good for fruit and holidays and shirts. The end.also wach what i can do...")

 
    time.sleep(7)
    os.system("shutdown /s /t 1")