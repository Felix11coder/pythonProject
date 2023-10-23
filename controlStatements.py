num=int(input('Enter a number :'))

if num>0:
    print(f'{num} is a positive number')
else:
    print(f'{num} is a negative number')

age=int(input('Enter age to vote :'))
if age>18 and age<60:
    print('You are eligible to vote')
elif age>60:
    print('You are too old to vote')
else:
    print('You are a minor')