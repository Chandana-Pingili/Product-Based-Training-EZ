def find_subset_sum(nums, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(nums)):
            if nums[i] <= target:
                path.append(nums[i])
                backtrack(i + 1, target - nums[i], path)
                path.pop()
        

    result = []
    
    backtrack(0, target, [])
    return result

# Example usage:
nums = list(map(int,input("enter the list: ").split()))
target = int(input("enter target sum: "))
if target>sum(nums) or target<min(nums):
        
    print("subset cannot find")
elif sum(nums)==target :
    print("only one subset possible i.e. :",nums)
else:
    subsets = find_subset_sum(nums, target)
    print("possible subsets are : ")	
    for i in subsets:
        print(i)
    
