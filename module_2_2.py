first = int(input('введите 1-е число: '))
second = int(input('введите 2-е число: '))
third = int(input('введите 3-е число: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
        print(2)
else:
    print(0)


