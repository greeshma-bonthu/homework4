nums=[1,2,2,7]
target=9
def twoSum(nums, target):
    for i in nums:
        for j in nums[nums.index(i)+1:]:
            if(i+j==target):
                return (nums.index(i), nums.index(j))


print(twoSum([1,2,3,7],9))




