 
import random 
def makeboard (List):
    for i in range (12):
        temp=[]
        for x in range (12): 
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
    
    for i in range (10):
        List [1] [2+i]="___"



def displayboard (List):
    for i in range (12):
        for x in range (12):
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
    if movement=="a":
        x=x-1
    if movement=="s":
        y=y+1
    if movement=="d":
        x=x+1
    
print("welcome to MANHOLE. YOU CAN FIGHT MOVE and more. spare for aurmour, kill for weapons.")
print(" if you find a infinite damegae glich press F3 to report it. also... we now every thing and can tell if you lie.")
print("please chose what your heart wants you to. we are taking your disions and making AI to take over the world.")
print("  when you have killed cpu? please ask did you get all that a we will respond also if you die in here you die in here. what did you think you would die out there nope.")
print( "i mean the AI will take oevr and your fate will be dersided then so...um /entermanholethegamecodeexe.net")


board=[]
makeboard (board)
displayboard(board)
