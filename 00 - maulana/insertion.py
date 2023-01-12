nums = [3,1,12,5,1,2,0,8,4]
print(nums,end="\n")
for i in range(len(nums)-1,1,-1):
    key = nums[i]
    print("--key",key,"--")
    iBefore = i-1
    while iBefore >=0 and nums[iBefore]>=key:
        print("key =",key,"Data[iBefore-1]=",nums[iBefore])
        nums[iBefore+1] = nums[iBefore]
        print("data pergeseran:",nums)
        
        print("iBefore:",iBefore)
    nums[iBefore+1] = key
    print("=> Data Sementara=",nums)
