def incrementer() :
    i = 1
    while True :
        yield i
        i += 1

inc = incrementer()
print( next( inc ) )
print( next( inc ) )
print( next( inc ) )

for i in inc:
        if (i<30):
            print (i)
        else:
             break

print ("Hello There")



