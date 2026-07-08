
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
sanke=randint(0, 19)
s=randint (0, 19)
lis [sanke][s]="🐍"
for q in range (0, 20):
    print ("")
    for w in range (0, 20):

        if  q==sanck[0]and w==sanck[0]:
            print ("s",end="")
        else:print (lis[q][w],end="")
    


#def move ()




#board=[]

#akeboard(board)
#board [x][y]="🐍"
print (plalislf)
print(plalisud)