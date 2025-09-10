def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter the value of n: "))
l = list(range(1, n + 1))
a = [i for i in l if is_prime(i)]

print("List from 1 to n:", l)
print("Prime numbers in the list:", a)
