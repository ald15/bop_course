import random
a = 0
n = 0
o = 0
o1 = 0
o2 = 0
answer = 0
point = 0
correct = 0
incorrect = 0
attempt = 0
while a not in (1,2,3):
  a = int(input("Введите уровень сложности: "))
  if a < 0:
    print("Уровень сложности должен быть от 1 до 3")
  elif a >= 4:
    print("Уровень сложности должен быть от 1 до 3")
  elif a == 1: 
    n = [1,11]
  elif a == 2:
    n = [1,51]
  elif a == 3:
    n = [1,101]
print("Выбранный уровень сложности: ", a, n)
for i in range(1, 6):
  s = (f"{random.randint(n[0], n[1])}{random.choice("-+*")}{random.randint(n[0], n[1])}")
  print(s)
  o = eval(s) 
  answer = (input("Введите ваш ответ: "))
  if answer == "стоп":
      break
  if  int(answer) == o:
    correct += 1
    point += 10
    print("Попал!!!")
  else:
    incorrect +=1
    point -=3
    if point < 0:
      point = 0
    print("Правильный ответ: ", o, "Ваш ответ: ", int(answer), "Расходжение: ", abs(int(answer) - o))
  attempt +=1
if attempt > 0:
  print("Количество примеров: ", attempt)
  print("Количество правильных ответов: ", correct)
  print("Количество неправильных ответов: ", incorrect)
  print("Процент правильных ответов: ", correct/attempt*100, "%")
  print("Процент неправильных ответов: ", incorrect/5*100, "%")
  print("Набрано баллов: ", point)
else:
  print("Нет ответов")
if point == 50:
  print("Успешно вычислены все примеры")
