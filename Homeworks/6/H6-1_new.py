import random as r

difficult = 0  # Уровень сложности
N = 5  # Количество примеров
answer = None  # Пользовательский ответ
correct = 0  # Количество верно решенных примеров
baseDifficults = {
    '1': [1, 11],
    '2': [1, 51],
    '3': [1, 101]
}  # Диапазоны чисел относительно уровня сложности

while True:
    difficult = input("Введите уровень сложности: ")
    if difficult in baseDifficults.keys():
        break
    print("Уровень сложности должен быть от 1 до 3")
print("Выбранный уровень сложности: ", difficult)

for i in range(N):
    # Формирование выражения
    s = f"{r.randint(*baseDifficults[difficult])}{r.choice('-+*')}{r.randint(*baseDifficults[difficult])}"
    print(s)
    result = eval(s)
    answer = input("Введите ваш ответ (или стоп): ")
    if answer == "стоп":
        break
    elif int(answer) == result:
        correct += 1
    else:
        print(
            f"Правильный ответ: {result}. Ваш ответ: {answer}. Расходжение: {abs(int(answer) - result)}")
if i > 0:
    solved = i + 1
    points = max(correct * 10 + (solved - correct) * (-3), 0)
    print(f"Количество примеров: {solved}")
    print(f"Количество правильных ответов: {correct}")
    print(f"Количество неправильных ответов: {solved - correct}")
    print(f"Процент правильных ответов: {correct / solved * 100}%")
    print(
        f"Процент неправильных ответов: {(solved - correct) / solved * 100}%")
    print(f"Набрано баллов: {points}")
else:
    print("Нет ответов")
if correct == N:
    print("Успешно вычислены все примеры!")
