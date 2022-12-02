t = ('A','B','C')
print(t)

t1 = tuple(('A','B','C'))
print(t1)

t2 = ('A',)  # str
print(type(t2))

t3 = (1,[2,3],4)
print(t3[0],t3[1],t3[2])    # 1 [2, 3] 4
print(t3[1],type(t3[1]))    # [2, 3] <class 'list'>

t3 = (1,[2,3],4)
for item in t3:
    print(item)