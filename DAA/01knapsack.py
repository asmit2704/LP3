n = int(input("Enter number of items: "))

values = list(map(int, input("Enter values: ").split()))
weights = list(map(int, input("Enter weights: ").split()))

W = int(input("Enter knapsack capacity: "))

if n <= 0 or len(values) != n or len(weights) != n:
    print("Invalid input")
elif W < 0 or any(w <= 0 for w in weights):
    print("Invalid capacity or weights")
else:
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                values[i] + dp[w - weights[i]]
            )

    print("Maximum profit:", dp[W])