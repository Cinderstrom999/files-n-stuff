x=1
y=1 
import random 
def makeboard (List):
    for i in range (20):
        temp=[]
        for x in range (20): 
            temp.append (" - ")
        List.append (temp)
    List [6] [5]="[-]"
    List [5] [5]="cpu" 
    List [7] [5]="cpu"
    List [5] [8]="[-]"
    List [4] [8]="cpu"
    List [11] [0]="cpu"
    List [11] [1]="?- "
    List [10] [10]="[-]"
    List [9] [10]="cpu"
    List [1] [0]="___"
    List [1] [1]="_  " 
    List [3] [1]="[-]"
    List [3] [2]="loo"
    List [3] [3]="t- "
    List [8] [2]="[-]"
    List [9] [6]="[-]"
    List [9] [7]="cpu"
    List [10] [3]="fun"
    List [19] [18]="nom"
    List [19] [19]="win"
    List [12] [4]="cols"
    List [15] [10]="[__"
    List [14] [10]=" __"
    List [15] [11]="___" 
    List [14] [11]="___"
    List [14] [12]="___"
    List [14] [13]="___"
    List [14] [14]="___"
    List [14] [15]="___"
    List [14] [16]="___"
    List [15] [12]="___"
    List [15] [13]="___"
    List [15] [14]="___"
    List [15] [16]="___"
    List [15] [15]="___" 
    List [15] [17]="___"
    List [15] [18]="___"
    List [15] [19]="_:)"
    List [14] [19]="_  "
    List [14] [17]="___"
    List [14] [18]="___"
    List [17] [5]="far"
    List [17] [6]=""
    List [17] [6]="tls"
    List [13] [0]="₡  "
    List [13] [1]="ↈ↉↊"
    List [13] [2]="⎱⎲⎳"
    List [13] [3]="☢☣☤"
    List [13] [3]="⚒⚓⚔"
    List [13] [4]="⚦⚧⚨"
    List [13] [5]="⎙⎚⎛"
    List [13] [6]="⌚⌛⌜"
    List [13] [7]="№℗℘"
    List [13] [8]="⇴⇵⇶"
    List [13] [9]="…†‡"
    List [13] [10]="⛳⛴⛵"
    List [13] [11]="☸☹☺"
    List [13] [12]="♧♨♩"
    List [13] [13]="hum"
    List [13] [14]="dif"
    List [13] [15]="ity"
    List [13] [16]="4"
    List [13] [17]="lif"
    List [13] [18]="e y"
    List [13] [19]="ay$"
  
    
    
    
    
    
     
    
    
     
    
    
    
    
    for i in range (18):
        List [1] [2+i]="___"



def displayboard (List):
    for i in range (20):
        for x in range (20):
            print (List[i][x],end="")
        print()

def attack(weapon, target, cpu):
    rand=random.randint(0,weapon)
    swoon=random.randint(0,100)
    if cpu:
        chance=50 
    else:
        chance=5
    if swoon <chance:
        print ("SWOON")
        rand=999

    target=target-rand 
    print ("!"+str(rand)+"!" )

def reason(reason,index):
    qwestions=[["stop, get some help","i will pay your tab","tx 4 da good +vice","!i will!","can [i] ge(t) a [aou}togra{f]","DOnotopenthedoor","never say ee or hey will ax us"],
    ["your doing fine","how a bout a bank loan","thanks for the good addvice", "what?","are u a big[shot]?","do not open the door ", "do not say t or they will tax uou for money!"],
    ["you look great!","just fined some money on the side of the street","you need some major gramor lessons!","i will not", "just keep telling your self things", "but i want to open the door so i will", "but t is a important part of the englsih language i will use till i leve this tttt filled planet "]] 
    print ("1: "+ qwestions[0][index])
    print ("2: "+ qwestions[1][index])
    print ("3: "+ qwestions[2][index])
    pick=input("pick 1,2,3")
    if pick==1:
       if index==6:
           print ("u win yay good for you have a good ime in he res of...he game")
       else:
           print ("u win yay good for u have a good time in the rest of... tHe GamE") 
       return "e"
    if pick==2:
        print("try again miss close but close, ok try again, u will now be dameged, wow that looks pretty bad for! u yes i know im bad at small talk, but i am a computer so cut me some slack, ok try again")
        return "i"
    if pick==3:
        print("wrong u did very bad ok now u can only attack no mre spareing for u dont even try.  ")
        return "f"
    
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
    
    
board=[]
makeboard(board)
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

    