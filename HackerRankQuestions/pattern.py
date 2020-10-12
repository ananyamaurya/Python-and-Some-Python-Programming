
for i in range(1, int(input())+1):
    print(''.join([str(x) for x in range(1,i+1)]), ''.join([str(x) for x in range(i-1, 0, -1)]),sep='')
