
def binarySearch(nums, target):
    # Write your code here
    start=0
    end=len(nums)-1
    mid=(start+end)//2
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
          return mid
        elif nums[mid]>target:
          end=mid
        else:
          start=mid+1
        if start+end==2*mid: # this will break if list iterate till last 
          break
    return -1
