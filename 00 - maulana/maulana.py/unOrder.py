def unOrder(list,key):
    found=False
    i=0
    while i<len(list) and not(found):
        if list[i]==key:
            ind=i
            found=True
        i+=1
    if found:
        return ind
    else:
        return False

a=[54,25,73,12,15,2,30]
unOrder(a,73)

        