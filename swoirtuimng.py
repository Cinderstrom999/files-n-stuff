import random
import queue
import webbrowser
import time
lis=[]
rue=False
tr1=0
while True:

    
    sadf=random.randint (0, 108)
    for yy in range (tr1):
        if sadf<=lis[yy]:
            lis.insert (yy, sadf)
            rue=True
        print (sadf)
    if rue==False:
        lis.append(sadf)
    tr1+=1
    time.sleep (0.5)
    
#    asdf=random.randint(0, 999999)
#     if asdf==67 or asdf==69:
#         import os
#         import time
    

#         import signal
#         import playsound3 
#         plalislf=0
#         signal.signal(signal.SIGINT,lambda:0)
#         signal.signal(signal.SIGTERM,lambda:0)
#         while True:
#             signal.signal(signal.SIGINT,lambda:0)
#             signal.signal(signal.SIGTERM,lambda:0)
#             os.system ("start chrome --new-window \"https://undertale.wiki/w/Sans\" ")
#             os.system ("start chrome --new-window \"https://guthib.com/\" ")