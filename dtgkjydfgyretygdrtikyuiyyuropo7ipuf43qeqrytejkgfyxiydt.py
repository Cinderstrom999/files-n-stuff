
import random
plalislf=0
plalisud=0
L=3
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
    global plalisud, plalislf
    if wasd=="w":
        plalisud+=1

    if wasd=="a":
        plalislf-=1
    
    if wasd=="s":
        plalisud-=1


    if wasd=="d":
        plalislf+=1
    if wasd=="h":
        score+=1000
    if wasd=="q" or wasd=="e":
        score-=1000
lis=[]
sanck=(0,0)
for i in range (0, 20):
    temp=[]
    for j in range (0, 20):
        temp.append(" - ")
         
    lis.append (temp)
sanke=random.randint(0, 19)
s=random.randint (0, 19)
lis [sanke][s]="🐍"






#def move ()




#board=[]

#akeboard(board)
#board [x][y]="🐍"
print(plalislf)
print(plalisud)
while True:
    print ("hehe i printed but not the other ones",plalislf, plalisud,)
    (dufffffffffffffffff)=(input("w a s or d qERGAqergtoihaqteg  ;nadergik;ufdashjgv        "))
    if dufffffffffffffffff=="w" or dufffffffffffffffff=="a" or dufffffffffffffffff=="s" or dufffffffffffffffff=="d":
        brooklyen(dufffffffffffffffff)

        for q in range (0, 20):
                print ("")
                for w in range (0, 20):

                    if  q==plalislf and w==plalisud:
                        print ("s",end="")
                    else:print (lis[q][w],end="")

