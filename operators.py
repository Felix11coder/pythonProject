#arithmetic operators
x=6
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)

#Comparison operators
a=12
b=34

print(f'{a} is equal to {b}= {a==b} ')
print(f'{a} is not equal to {b}= {a!=b} ')
print(f'{a} is greater than or equal to {b}={a>=b}')
print(f'{a} is less than or equal to {b}={a<=b}')

#logical operators
c=5
print(f"is this statement true= {c>2 and c<5}")
print(f'one of the conditions is true= {c>2 or c<5}')

a=35
b=6
c=a/b
print(c)
print(c.__ceil__())