name = input("Введие число ")
first = 10
second = 10
third = 10

if first == second == third:
    print(2)
elif first == second != third or first == third != second or second == third != first:
    print(3)
else:
    print(0)
