# WAP to check the given year is leap or not

a = int(input('Enter the year : '))

if ((a % 4 == 0 and a % 100 != 0) or (a % 400 ==0)):
    print(a, 'is leap year')
else:
    print(a, 'is not leap year')