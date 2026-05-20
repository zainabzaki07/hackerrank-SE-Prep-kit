

def findFirstOccurrence(nums, target):
    # Write your code here
    if target not in nums:
        return -1
    else:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
