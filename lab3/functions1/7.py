def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

has_3 = list(map(int, input().split()))
print(has_33(has_3))