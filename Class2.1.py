nums = [1, 3, 5, 1, 8, 0]
print(nums[-1])
print(nums[1:3]) # first - inclusive, last - exclusive
print(nums[:3])
print(nums[3:])
nums[0] = 99
print(nums)
nums.append(7)
print(nums)
nums.remove(7)
print(nums)
nums.pop(1)
print(nums)
print(len(nums))

for num in nums:
    print(num*2)

print("==========")

print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)

sum = sum(nums)
print("sum: " , sum)
min = min(nums)
print("min: " , min)
max = max(nums)
print("max: " , max)