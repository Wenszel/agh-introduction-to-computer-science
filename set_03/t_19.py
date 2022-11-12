from random import randint


def f(t):
    max_length = 0

    for i in range(len(t)):
        j = i + 1
        sum_of_values = t[i]
        sum_of_indexes = i
        length = 1
        while j < len(t) and t[i] < t[j]:
            length += 1
            sum_of_values += t[j]
            sum_of_indexes += j
            j += 1
            if sum_of_indexes == sum_of_values and max_length < length:
                max_length = length
    return max_length


n = int(input("n: "))
array = [randint(1, 1000) for _ in range(n)]
print(f(array))
