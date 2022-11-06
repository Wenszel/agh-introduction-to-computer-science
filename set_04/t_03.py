from random import randint


def has_any_even_digit(number):
    while number > 0:
        if number % 10 % 2 == 0:
            return True
        number //= 10
    return False


def check_rows(table, length):
    for i in range(length):
        flag = True
        for j in range(length):
            if not has_any_even_digit(table[i][j]):
                flag = False
        if flag:
            return True
    return False


l = int(input("Array length: "))
t = [[randint(1, 10 ** 5) for _ in range(l)] for _ in range(l)]
print("\nThe array:")
for i in t:
    for j in i:
        print(j, end=" ")
    print("")
print("\nIs there a row in the array in which each number contains at least one even digit? \n", check_rows(t, l))



