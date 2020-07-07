arr=[1,2,3,4,5,4,3,2,1,3,4]

def migratoryBirds(arr):
    arrcount =[0,0,0,0,0]
    for i in range(len(arr)):
        if(arr[i]==1):
            arrcount[0]= arrcount[0]+1
        if(arr[i]==2):
            arrcount[1]= arrcount[1]+1
        if(arr[i]==3):
            arrcount[2]= arrcount[2]+1
        if(arr[i]==4):
            arrcount[3]= arrcount[3]+1
        if(arr[i]==5):
            arrcount[4]= arrcount[4]+1
    return (arr.index(max(arrcount)))+1
result = migratoryBirds(arr)
print(result)
 
