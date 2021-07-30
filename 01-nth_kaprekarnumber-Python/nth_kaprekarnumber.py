# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.

import math

def fun_nth_kaprekarnumber(a):
    start=1
    end=10000
    l=[]
    co=0
    if a==0:
        l.insert(co,1)
        co+=1
    for i in range(start, end + 1):
        sqr = i ** 2
        digits = str(sqr)
        length = len(digits)
        for x in range(1, length):
            left = int("".join(digits[:x]))
            right = int("".join(digits[x:]))
            if (left + right) == i:
                l.insert(co,str(i))
                co+=1
                #print("Number: " + str(i) + "Left: " + str(left) + " Right: " + str(right))
    return int(l[a])


  
    

    