name = input("name: ")
age = input("age:")
msg = f"""
!----
    name: {name}
    age: {age}
----!
"""
print(msg)
print(type(name),type(age)) # <class 'str'> <class 'str'>