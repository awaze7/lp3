class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):

    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    finalvalue = 0.0

    for item in arr:

        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit

        else:
            finalvalue += item.profit * W / item.weight
            break

    return finalvalue


def main():
    # W = 50
    # arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    
    W = int(input("Enter the knapsack weight (W): "))
    num_items = int(input("Enter the number of items: "))
    
    arr = []
    for i in range(num_items):
        profit = int(input(f"Enter the profit for item {i+1}: "))
        weight = int(input(f"Enter the weight for item {i+1}: "))
        arr.append(Item(profit, weight))
    
    max_val = fractionalKnapsack(W, arr)
    print(f"Maximum total profit in the knapsack: {max_val}")

if __name__ == "__main__":
    main()
