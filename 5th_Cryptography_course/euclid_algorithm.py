def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 150000
num2 = 5055
result = gcd(num1, num2)
print("GCD of", num1, "and", num2, "is:", result)
