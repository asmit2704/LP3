n = int(input("Enter number of items: "))

values = list(map(int, input("Enter values: ").split()))
weights = list(map(int, input("Enter weights: ").split()))

capacity = float(input("Enter knapsack capacity: "))

if n <= 0 or len(values) != n or len(weights) != n:
    print("Invalid input")
elif any(w <= 0 for w in weights) or capacity < 0:
    print("Weights must be positive and capacity non-negative")
else:
    items = list(zip(values, weights))

    # Sort by value/weight ratio
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_profit = 0

    for value, weight in items:
        if capacity <= 0:
            break

        take = min(weight, capacity)

        total_profit += take * (value / weight)
        capacity -= take

    print("Maximum profit:", total_profit)