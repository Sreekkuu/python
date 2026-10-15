a=[1,2,3,4,5]
b=[c**2 for c in a]
print(b)
a=[x for x in range(1,6)]
print(a)
fruits=['apple,banana,orange']
upper=[fruit.upper() for fruit in fruits]
print(upper)
a=[1,2,3,4,5,6,7,8]
b=[c for c in a if c %2 == 0]
print(b)
a=[10,20,30,13]
b=[c for c in a if c>10]
print(b)