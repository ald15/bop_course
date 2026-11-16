mes = input("Мой генерал! Мы получили новое сообщение!: ")
st1 = mes.strip('#*!')
st2 = st1.replace("_"," ")
st3 = st2[::-1]
st4 = st3.lower()
if "тревога" in st4:
  print("СРОЧНОЕ СООБЩЕНИЕ!!!!!!!!!!!!!!!!!!!!!!")
print(st4)
