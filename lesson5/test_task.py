age = input('How old are you?: ')  # '18'
print(int('1') + 2)
print(str(2))  # '2' -> 2

try:
    age = int(age)
    if age >= 18:
        print('You are adult')
    else:
        print('You are infant yet')
except ValueError:
    print(f'{age} is not a number')



a = 2 / 1
print(a)
for i in range(16):
    print('{:^10} | {:^10} | {:^10}'.format(i, i, i))

age = 18
print('hello world')