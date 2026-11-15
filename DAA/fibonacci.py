# Iterative Fibonacci
def fibonacci_iterative(n):
    a, b = 0, 1

    for i in range(n - 1):
        a, b = b, a + b

    return a


# Recursive Fibonacci
def fibonacci_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input("Enter n: "))

print("Iterative:", fibonacci_iterative(n))
print("Recursive:", fibonacci_recursive(n))