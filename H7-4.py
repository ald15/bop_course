mage1 = input("Your spell, Gandalf: ")
count1 = 0
if "огонь" in mage1.lower():
  count1 +=10
if "лед" in mage1.lower():
  count1 +=10
if "молния" in mage1.lower():
  count1 +=10
for i in range(len(mage1)):
  if ord(mage1[i]) in range(1040, 1104):
    count1 += 1 
  elif ord(mage1[i]) in range(48, 58):
    count1 +=int(mage1[i])
mage2 = input("Your spell, Saruman: ")
count2 = 0
if "огонь" in mage2.lower():
  count2 +=10
if "лед" in mage2.lower():
  count2 +=10
if "молния" in mage2.lower():
  count2 +=10
for i in range(len(mage2)):
  if ord(mage2[i]) in range(1040, 1104):
    count2 += 1 
  elif ord(mage2[i]) in range(48, 58):
    count2 +=int(mage2[i])
print("Сила первого заклинания: ", count1)
print("Сила второго заклинания: ", count2)
if count1 > count2:
  print("Победил маг №1")
elif count1 < count2:
  print("Победил маг №2")
else:
  print("Могущество ваше соразмерно!!!")