from random import randint


def has_only_odd_digits(number):
    while number > 0:
        if number % 10 % 2 == 0:
            return False
        number //= 10
    return True


def check_rows(table, length):
    for i in range(length):
        flag = False
        for j in range(length):
            if has_only_odd_digits(table[i][j]):
                flag = True
        if not flag:
            return flag
    return True


l = int(input("Array length: "))
t = [[randint(1, 10 ** 5) for _ in range(l)] for _ in range(l)]
print("\nThe array:")
for i in t:
    for j in i:
        print(j, end=" ")
    print("")
print("\nIs there at least one number in each row of the array composed of only odd numbers? \n", check_rows(t, l))



