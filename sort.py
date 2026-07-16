lis=[45, 22,97,2,88,77,1]
lis2=[]
len(lis)
folk=-1
folk2=0
for yy in range (0, len(lis)-1):
    minalmal=lis[yy]
    i=yy
    print (minalmal)
    for qq in range (yy, len (lis)):
        if lis[qq]<minalmal:
                minalmal=lis[qq]
                temp=lis[qq]
                lis2=lis[qq]
                if lis2-1>minalmal:
                    lis.append
                elif lis2-1<minalmal: 
                    lis2.append(minalmal)

                
print (lis)
print (lis2)