# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def readArray():
    t = input().split(" ")
    L = []
    for i in t:
        if len(i) != 0:
            L.append(int(i))
    return L

def smallestdifference(a):
    if(a==[]):
        return(-1)
    c=10**20
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(abs(a[i]-a[j])<c):
                c=abs(a[i]-a[j])
    return (c)
    