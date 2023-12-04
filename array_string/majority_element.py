def majority_element(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[n//2]

print(majority_element(nums = [2,2,1,3,5,6,7,8,9]))