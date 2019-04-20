def partion(nums,left,right):
    key = nums[left]
    while left < right:
        while left < right and nums[right] >= key:
            right -= 1
        while left < right and nums[left] < key:
            left += 1
        if left < right:
            nums[right],nums[left] = nums[left],nums[right]

    return left


def quick_sort_standard(nums,left,right):
    if left < right:
        key_index = partion(nums,left,right)
        quick_sort_standard(nums,left,key_index)
        quick_sort_standard(nums,key_index+1,right)

if __name__ == '__main__':
    nums = [5, 6, 4, 2, 3,1]
    print (nums)
    quick_sort_standard(nums,0,len(nums)-1)
    print (nums)