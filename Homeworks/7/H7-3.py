l = input()
ins  = l.split(";")
im = str()
doc = str()
dan = str()
count = 0
dan_count = 0
mask_count = 0
for i in range(len(ins)):
 
  if ".exe" in ins[i].lower() or ".bat" in ins[i].lower() or ".cmd" in ins[i].lower() :
   dan = ins[i]
   print(dan, " - Опасный файл")
   dan_count += 1
   if dan.count(".") > 1:
       print(dan, " - Опасный файл, Маскировка!")
       mask_count += 1 

  elif ".jpg" in ins[i].lower() or ".png" in ins[i].lower() or ".gif" in ins[i].lower() :
   im = ins[i]
   print(im, " - Изображение")

  elif ".txt" in ins[i].lower() or ".pdf" in ins[i].lower() or ".docx" in ins[i].lower() :
   doc = ins[i]
   print(doc, " - Документ")  


  else: 
    print(ins[i], "- Неизвестный файл")
  count +=1
print("Всего файлов: ", count)
print("Опасных файлов: ", dan_count)
print("Замаскированных файлов: ", mask_count)