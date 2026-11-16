# Iterative approach
def iterative(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Recursive approach
def recursive(n):
    if n <= 1:
        return n

    return recursive(n-1) + recursive(n-2)


# Main program
n = int(input("Enter n: "))

print("Iterative:", end=" ")
iterative(n)

print("\nRecursive:", end=" ")
for i in range(n):
    print(recursive(i), end=" ")

print()