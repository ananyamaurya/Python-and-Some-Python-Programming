s = 'UDDDUDUUUUDDU'
n=8
def countingValleys(n, s):
    valleycount =0
    count = 0
    for i in s:
        if(i == 'D'):
            valleycount = valleycount-1
        if(i == 'U'):
            valleycount = valleycount+1
            if(valleycount == 0):
                count = count+1

    print(count)
countingValleys(n,s)
