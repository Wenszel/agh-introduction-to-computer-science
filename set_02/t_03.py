def reverse(x):
    output = 0
    while x > 0:
        output *= 10
        output += x % 10
        x //= 10
    return output


n = int(input())
print(n == reverse(n))
bin_n = 5
while n > 0:
    bin_n = bin_n * 10 + n % 2
    n //= 2
bin_n = bin_n * 10 + 5
print(bin_n)

print(reverse(bin_n) == bin_n)
