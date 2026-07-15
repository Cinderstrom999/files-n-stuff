lis=[]
lis2=[]
number=1
for yy in range (2, 1000000):
    number+=1
    lis.append(number) 
for i in lis:
    steak=True
    for j in range(2, i):
        if i % j==0:
            steak=False
    if steak==True:
        lis2.append(i)
        print (lis2)
print (lis2)

    