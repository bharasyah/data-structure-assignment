a= [5,2,4,1,17,69,420]

def maksimal(bil):
    n_terbesar = bil[0]

    for n in bil:
        if n > n_terbesar:
         n_terbesar = n

    return n_terbesar

def minimal(bil):
    n_terkecil = bil[0]

    for n in bil:
      if n < n_terkecil:
        n_terkecil = n

    return n_terkecil


print (a)
print ("nilai terbesar adalah :", maksimal(a))
print ("nilai terkecil adalah:", minimal(a))
