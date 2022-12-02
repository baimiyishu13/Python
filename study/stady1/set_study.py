s = {'A','B','C'}
s2 = set(range(10))
print(s)            # {'A', 'C', 'B'}
print(s2)           # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

s3 = set([1,2,3,4])
print(s3,type(s3))  # {1, 2, 3, 4} <class 'set'>

s4 = set((1,2,3,4))
print(s4)           # {1, 2, 3, 4}

s5 = set('Python')
print(s5)           # {'t', 'P', 'n', 'h', 'o', 'y'}

S0 = {i for i in range(1,10)}
print(S0)