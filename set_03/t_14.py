from random import randint
n = int(input("Amount of people: "))
in_same_day = 0
not_in_same_day = 0
for _ in range(0, 10 ** 5):
    number_of_people_born = [0 for _ in range(365)]
    for i in range(n):
        number_of_people_born[randint(0, 364)] += 1
    if max(number_of_people_born) > 1:
        in_same_day += 1
    else:
        not_in_same_day += 1
print(in_same_day / (in_same_day + not_in_same_day))
