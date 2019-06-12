# Leetcode 53. Maximum Subarray

def maxSubArray_Greedy_1(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Greedy Algorithm
    # For each element, compare with previous sum. Take the larger value as local max
    # (Abandon the string when not helping for increase the value)
    # Then keep the global max
    local_sum = nums[0]
    global_sum = nums[0]
    
    for idx in range(1, len(nums)):
        
        if  nums[idx] + local_sum > nums[idx] :
            local_sum = nums[idx]  + local_sum
        else:
            local_sum = nums[idx] 
            
        if local_sum > global_sum:
            global_sum = local_sum
            
    return global_sum

def maxSubArray_Greedy_2(self, nums):
    # Simplify Greedy
    local_sum = global_sum = nums[0]
    for idx in range(1, len(nums)):
        
        local_sum = max(nums[idx], nums[idx] + local_sum)
        global_sum = max(global_sum, local_sum)
            
    return 

def maxSubArray_DynamicProgramming(self, nums):
    # Dynammic Programming Solution
    # Sub problem: Is previous value benificial?
    # Yes: Replace current value w/ previouse, string will be added if keeps increasing
    # No: Abandon previous string, start new one
    n = len(nums)
    max_sum = nums[0]
    for i in range(1, n):
        if nums[i - 1] > 0:         # Check if previous value larger than 0
            nums[i] += nums[i - 1]  

        max_sum = max(nums[i], max_sum)

    return max_sum
