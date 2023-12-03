# desafio:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

def sum_two(nums: list[int], target: int) -> list[int]:
    """
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def hash_table_two_sum(nums: list[int], target: int) -> list[int]:
    """A hash table is a data structure which stores key-value pairs,
    a value can be looked up with a given key in constant time.
    """

    # Our hash table that stores at which index the number is at
    numToIndex = {}

    # 1. Iterate over every number in the array
    for i in range(len(nums)):
        # 2. Calculate the complement that would sum to our target
        complement = target - nums[i]
        print(f"complement:{complement}")

        # 3. Check if that complement is in our hash table
        if complement in numToIndex:
            print(f"numToIndex[complement]:{numToIndex[complement]}")
            print(f"i:{i}")
            return numToIndex[complement], i

        # 4. Add the current number to our hash table
        numToIndex[nums[i]] = i
        print(f"numToIndex[nums[i]]:{numToIndex[nums[i]]}")
    print(numToIndex)

# print(sum_two(nums=[3, 9, 18, 20, 1, 17], target=18))
print(hash_table_two_sum(nums=[3, 9, 18, 20, 1, 17], target=18))
