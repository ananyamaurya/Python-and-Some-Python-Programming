scores =[10,5,20,20,4,5,2,25,1]

def breakingRecords(scores):
    maxt= scores[0]
    mint= scores[0]
    maxcount=0
    mincount=0
    for i in range(1,len(scores)):
        if(maxt<scores[i]):
           maxcount=maxcount+1
           maxt=scores[i]
        if(mint>scores[i]):
           mincount = mincount+1
           mint=scores[i]
    print(maxcount,'  ',mincount)

    
breakingRecords(scores)
