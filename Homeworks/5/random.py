import random
n = int(input("Введите количество бросков: "))
m = 0
k = 2
g = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, n):
  a = random.randint(1,6)
  b = random.randint(1,6)
  s = a+b
  m += s
  if s > k:
    k=s
  #print("(", a,",", b, ")", sep = '',end=" ")
  #print(s)
  g[s-2] += 1
for j in range(len(g)):
  g[j] /= n
print("Сумма всех бросков: ", m)
print("Максимальное значение броска: ",k)

print("Частота значений: (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)", g)