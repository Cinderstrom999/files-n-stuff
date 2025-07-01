 

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
    for i in range (10):
        List [1] [2+i]="___"



def displayboard (List):
    for i in range (12):
        for x in range (12):
            print (List[i][x],end="")
        print()

board=[]
makeboard (board)
displayboard(board)
