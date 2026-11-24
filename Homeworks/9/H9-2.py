nums = [1, 2, 4, 34, 234, 7, 2, 9, 10]
even_nums = []
for i in range(len(nums)):
  if nums[i]%2 == 0:
    even_nums.append(nums[i])
print(even_nums)
if 6 not in even_nums:
  even_nums.append(6)
print(even_nums)
print(even_nums[:2], even_nums[-3:])
print(len(even_nums))
print(nums)