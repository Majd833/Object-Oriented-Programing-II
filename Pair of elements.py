class pair_elements:
    def twoSum(self,nums,value):
        lookup={}
        for i,num in enumerate(nums):
            if value - num in lookup:
                return(lookup[value-nums])
            lookup[nums]=i
value=int(input("Enter a number to be searched:"))
print("Index1=%d ,Index2=%d" %pair_elements().twoSum((10,20,30,40,50,60,70),value))