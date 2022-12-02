scores = {'name':'A', 'age': 19 }
scores2 = dict(name='A', age =19 )
print(scores,scores2)

a = scores['name']
b = scores.get('age')

print(a,b)

print('name' in scores) # True

del scores['age']
print(scores)   #{'name': 'A'}

scores['addr'] = 'china'
print(scores)   # {'name': 'A', 'addr': 'china'}

print(scores.keys())    # dict_keys(['name', 'addr'])
values = scores.values()
print(list(values))     # ['A', 'china']

print(scores.items())   # 元组：dict_items([('name', 'A'), ('addr', 'china')])


for i  in scores:
    print(i)        # 获取的为 key

for i  in scores:
    print(i,scores[i])
    print(i,scores.get(i))

items = ['a','b','c']
num = [1,2,3]
lst = zip(items,num)
print(list(lst))    # [('A', 1), ('B', 2), ('C', 3)]

items = ['a','b','c']
num = [1,2,3]
d = { items.upper():num for items,num in zip(items,num)}
print(d)        # {'A': 1, 'B': 2, 'C': 3}