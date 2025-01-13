a = int(input("a: "))
b = int(input("b: "))
k = int(input("k: "))

for n in range(a, b + 1):
    n_divisors = 0

    for i in range(1, n + 1):
        if n % i == 0:
            n_divisors += 1
            if n_divisors > k:
                break

    if n_divisors == k:
        print(n, end=" ")
