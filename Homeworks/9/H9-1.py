a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print('\n'.join([' '.join([str(i) for i in j]) for j in a ])) 
print(*[str(a[i]).strip('[]').replace(',','') for i in range(len(a))], sep = '\n') #- но тут есть sep 