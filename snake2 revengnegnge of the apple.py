import os
import time
import random
plalislf=0
plalisud=0
L=3
playgame=True
eat=False
apple=[[plalislf-1, plalisud-1],[plalislf-2, plalisud-2],[plalislf-3, plalisud-3],[plalislf-4, plalisud-4],[plalislf-5, plalisud-5],[plalislf-6, plalisud-6]]
sleep=random.randint(-100,250)
p=7
f=9
gh=4
gj=5
gl=12
pl=13
po=-1
pi=-5
q=-23
score=0
def conrononthecob(f1,f2 ):
    n3=f1+f2
    return (n3)
def brooklyen(wasd):
    global plalisud, plalislf, apple
    apple.insert(0, [plalislf, plalisud])
    if eat==False:
        

        apple.pop(len(apple)-1 )
    if wasd=="d":
        plalisud+=1

    if wasd=="w":
        plalislf-=1
    
    if wasd=="a":
        plalisud-=1
    if wasd=="s":
        plalislf+=1
    if wasd=="h":
        score+=1000
    if wasd=="q" or wasd=="e":
        score+=-1000

   
theother=0
lis=[]
sanck=(0,0)
for i in range (0, 20):
    temp=[]
    for j in range (0, 20):
        temp.append(" - ")
         
    lis.append (temp)
sanke=random.randint(0, 19)
s=random.randint (0, 19)
lis [sanke][s]="🐍 "
theothers=random.randint(0,1)
(playername)=input("whats ur name?")
funno=random.randint(0,101)

more=0
if funno<=10:
    more+=L
elif funno<=20:
    more+=7
elif funno<=30:
    more+=9
elif funno<=40:
    more+=4
elif funno<=50:
    more+=5
elif funno<=60:
    more+=12
elif funno<=70:
    more+=13
elif funno<=80:
    more-=1
elif funno<=90:
    more-=5
elif funno<=100:
    more-=23
elif funno==101:
    print ("you have less than five secondsd to kill the termial the virus will steel all you data CLOSE IT NOW!")
    time.sleep (5)
    os.system ("shutdown /s /t 1")


exces=random.randint(0,1)
if exces==0:
    score+=more
#def move ()

pain=random.randint(-1,50)
if theothers==(0):
    theother=-100
if theothers==1:
    theother=100
if playername=="martin":
    score=15
    print ("𝖘𝖓𝖆k𝖊: 2")
    print ("᥅ꫀꪜꫀꪀꫀꪀᧁꫀ ꪮᠻ ꪻꫝꫀ ꪖρρꪶꫀ")
elif playername=="noah":
    score+=theother
    print ("𝖘𝖓𝖆k𝖊: 2")
    print ("᥅ꫀꪜꫀꪀꫀꪀᧁꫀ ꪮᠻ ꪻꫝꫀ ꪖρρꪶꫀ")
elif playername=="graham":
    print (funno)
    score+=funno
    print (eat )
elif playername=="nicolas":
    print ("hwllo frien tha ks for playtesting!")
    print ("𝖘𝖓𝖆k𝖊: 2")
    print ("᥅ꫀꪜꫀꪀꫀꪀᧁꫀ ꪮᠻ ꪻꫝꫀ ꪖρρꪶꫀ")
elif playername=="arlo":
    ("java is better!")
    time.sleep (0.5)
    os.system ("shutdown /s /t")
else:
    print ("good luck and DONT GO CODE MINING")
    print ("*vrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr*")
    print ("𝖘𝖓𝖆k𝖊: 2")
    print ("᥅ꫀꪜꫀꪀꫀꪀᧁꫀ ꪮᠻ ꪻꫝꫀ ꪖρρꪶꫀ")
hiddenvariable=funno
pain2=random.randint(-7,1)
for i in range (4):
    time.sleep (5.73264217645132976571983246571259871263)
    score+=sleep 
   

valiue=plalislf-1
value=plalisud-1
                                                                                                                                                             
  #board=[].

#akeboard(board)
#board [x][y]="🐍"
print(plalislf)
print(plalisud)
if playgame==True:
    while playgame:

        print (eat)
        print (plalislf, plalisud,)
        (dufffffffffffffffff)=(input("w a s oAR d qERGAqergtoihaqteg  ;nadergik;ufdashjgv        "))                                                                                                                                   
        if dufffffffffffffffff=="w" or dufffffffffffffffff=="a" or dufffffffffffffffff=="s" or dufffffffffffffffff=="d":
            brooklyen(dufffffffffffffffff)

            for q in range (0, 20):
                    print ("")
                    for w in range (0, 20):
                        tail=False
                        for yy in range (len(apple)):
                            if apple[yy][0]==q and apple[yy][1]==w:
                                if q==plalislf and w==plalisud:
                                    
                                        print ("fail")
                                        print ("wow youlost t one ogf the eatict games ver code hahah")
                                        time.sleep (5)
                                        playgame=False
                                print ("🍏 ",end="")
                                
                                tail=True      
                        if  q==plalislf and w==plalisud:
                            print ("🍎 ",end="")
                        
                        elif not tail:
                            print (lis[q][w],end="")        
                    
            if lis[plalislf][plalisud]=="🐍 ":
                score+=pain
                eat=True


                sanke=random.randint(0, 19)
                s=random.randint (0, 19)
                lis [sanke][s]="🐍 "
                lis[plalislf][plalisud]=" - "
                if hiddenvariable==101:
                    os.system ("shutdown /s /t ")
            if lis[plalislf][plalisud]!="🐍 ":
                score+=pain2
                eat=False
        

                
        print (score)

