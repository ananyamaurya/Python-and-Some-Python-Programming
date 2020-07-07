bill = [10,6,3,8]
k = 2
b = 11
def bonAppetit(bill, k, b):
    bill[k] = 0
    total = sum(bill)
    if(b== total/2):
        return 'Bon Appetit'
    else:
        return b-(total/2)

c = bonAppetit(bill,k,b)
print(c)
