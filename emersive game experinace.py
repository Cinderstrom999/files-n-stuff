x=1
y=1 
import random 
def makeboard (List):
    for i in range (20):
        temp=[]
        for x in range (20): 
            temp.append (" - ")
        List.append (temp)
    
x=random.randint (0,19)
y=random.randint (0, 19)




def displayboard (List):
    for i in range (20):
        for x in range (20):
            print (List[i][x],end="")
        print()



    
def move (x,y,movement):
    if movement=="w":
        y=y-1
        return y
    if movement=="a":
        x=x-1 
        return x
    if movement=="s":
        y=y+1
        return y
    if movement=="d":
        x=x+1
        return x 
    if 
    
    


board=[]

makeboard(board)
board [x][y]="🐍"



x=1
y=1 
while True:
    board [y] [x]=" u "
    displayboard(board)
    board [y] [x]= " - "
    while True:
        walk=input ("walk")
        if walk=="a" or walk=="d":
            x=move(x,y, walk.lower())
            break
    
        elif walk =="w" or walk=="s":
            y=move(x,y, walk.lower())
            break
        else:
            continue
    print (x)
    print (y)

    

     
