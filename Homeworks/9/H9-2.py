nums = [1, 2, 4, 34, 234, 7, 2, 9, 10]
check = nums.copy()
even_nums = []
start = []
fin = []
for i in range(len(nums)):
  if nums[i]%2 == 0:
    even_nums.append(nums[i])
print(even_nums)
if 6 not in even_nums:
  even_nums.append(6)
print(even_nums)
for j in range(2):
  start.append(even_nums[j])
for h in range(3):
  fin.append(even_nums[len(even_nums)-(h+1)])
print(start, fin)
print(len(even_nums))
print(nums)