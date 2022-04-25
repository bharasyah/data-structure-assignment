a = [19,2,5,16,3,6,78]

def bs(n):

    for x in range (len(n)-1,0,-1):

        for y in range(x):
            if n[y]>n[y+1]:
                nn = n[y]
                n[y]=n[y+1]
                n[y+1]=nn
    
    return n

print ('sebelum diurutkan dengan bubbl sort: ',a )
print('setelah diurutkan dengan bubble sort: ', bs(a))
