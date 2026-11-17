import random
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
year = input("Введите год вашего рождения: ")
sh = input("Введите шаблон: ")
if len(name) <= 2:
  na = name
else:
  na = name[:2]
if len(surname) <= 3:
  sur = surname
else:
  sur = surname[:3]
ar = year[2:]
login = f"{na}{sur}{ar}"
if sh in login:
#  print(sh in login)
  print(f"{login}{random.randint(10,100)}")
else:
  print(login)