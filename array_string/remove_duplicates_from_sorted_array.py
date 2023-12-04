def remove_duplicates(nums: list[int]) -> int:
    nums2 = sorted(set(nums))
    return len(nums2), nums2

print(remove_duplicates(nums = [1,1,2,4,4,5,]))