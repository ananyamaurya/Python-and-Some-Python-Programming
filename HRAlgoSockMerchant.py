from collections import Counter
n = 9
socks = [10,20,20,10,10,30,50,10,20]
coun = Counter(socks)
c= list(coun.values())
count=0
for i in c:
    if( i%2 == 0):
        count= count+ int(i/2)
    else:
        count = count + int((i-1)/2)
print(count)
