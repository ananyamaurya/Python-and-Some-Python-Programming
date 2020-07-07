n = 6
p = 2
def pageCount(n, p):
    if(p-0 > n-p):
        return int((n-p)/2)
    else:
        return int((p-0)/2)

c = pageCount(n,p)
print(c)
