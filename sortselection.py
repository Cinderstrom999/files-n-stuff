lis=[45, 22,97,2,88,77,1]

len(lis)
folk=-1
folk2=0
for yy in range (0, len(lis)-1):
    minalmal=1
    i=yy
    print (minalmal)
    for qq in range (yy, len (lis)):
        if lis[qq]<minalmal:
                minalmal=lis[qq]
                temp=lis[qq]
                lis=lis[qq]
                
                
print (lis)