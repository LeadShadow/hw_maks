
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
val = '1'


try:
    val = int(val)
    print(val > 0)
except ValueError:
    print(f'value {val} is not a number')
finally:
    print('this will be printed anyway')


