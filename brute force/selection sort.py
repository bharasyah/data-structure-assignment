a = [12,5,2,6,79,32,8,9,32,8,98]

def s (a): 

    for tujuan in range(len(a)-1,0,-1):
        max = 0

        for n in range(1,tujuan+1):
            maxxx = a[max]
            if maxxx < a[n]:
                max = n
        a[max],a[tujuan] = a[tujuan], a[max]
    
    return a



print ('sebelum diurutkan: ', a)
print ('setelah diurutkan: ', s(a))
