a=1
b=1.0
c='1'
print(a,type(a))
print(b,type(b))
print(c,type(c))

a=2
b=2.0
c='2'
print(a,type(a))
print(b,type(b))
print(c,type(c))

a=b=c=10
print("a-",a,"b-",b,"c-",c)

a=10
b=20
print(a+b)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)
print(fruits[1])
print(fruits[3])

numbers = [10, 20, 30, 40, 50]
numbers[2]=35
print(numbers)

colors = ("red", "green", "blue")
print(colors)

colors = ("red", "green", "blue", "yellow")
print(colors[0])
print(colors[-1])

colors = ("red", "green", "blue")
#colors[1]="orange"
#TypeError: 'tuple' object does not support item assignment

coordinates = (10, 20, 30)
x,y,z=coordinates
print(x,y,z)

colors = ("red", "green", "blue")
print("blue" in colors)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(len(days))

students={"Alice": 85, "Bob": 90, "Charlie": 78}
print(students)
print(students['Bob'])
students['David']=92
print(students)
students.pop("Charlie")
print(students)
students['Bob']=95
print(students)
print('Alice' in students.keys())
print(len(students))