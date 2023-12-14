
iNum=77
num=iNum
iCount=0
binNumbers=[0,0,0,0,0,0,0]

while iNum > 0:
    iNum=iNum>>1
    if(iNum>0):
        iCount+=1
    else:
         if(iNum==0):
            binNumbers.insert(iCount,"1")
            if(iCount>0):
                binNumbers.pop(0)
            iNum=num-(2**iCount)
            num=iNum
            iCount=0
binNumbers.reverse()
print(binNumbers)      
        



    


