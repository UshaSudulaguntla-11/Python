a = int(input("Enter a: "))
b = int(input("Enter b: "))
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
g = gcd(a, b)
lcm = (a * b) // g
print("GCD:", g)
print("LCM:", lcm)
