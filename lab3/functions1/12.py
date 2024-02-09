def histogram(nums):
    for i in nums:
        return (i * "*")
    
s = list(map(int, input().split()))
print(histogram(s))