def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # left = 0
    # right = len(nums) - 1
    # while left < right:
    #     a=0
    #     b=0
    #     mid = (left + right) // 2
    #     if nums[mid] > nums[0]:
    #         left = mid + 1
    #         a=a+1
    #         print("a",a)
    #     else:
    #         right = mid
    #         b = b + 1
    #         print("b",b)
    # return nums[left]
    left = 0
    right = len(nums) - 1
    while left<=right:
        mid = (left+right)//2
        if nums[mid]>nums[mid+1]:
            return nums[mid+1]

        if nums[mid-1]>nums[mid]:
            return nums[mid]

        if nums[mid]>nums[0]:
            left = mid+1
        else:
            right=mid


print(findMin([23,24,25,1,2,3,4]))