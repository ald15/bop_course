a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(*a, sep='\n')
#print(*[a[i] for i in range(len(a))], sep='\n')
print(*[a[i][j] for i in range(len(a)) for j in range(len(a))], sep='\n')