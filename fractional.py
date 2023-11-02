class Item:
    def __init__(self, name, profit, weight):
        self.name = name
        self.profit = profit
        self.weight = weight
        self.fract=0.0
        
def fractionalKnapsack(W, arr):

    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    
    knapsack=[]
    finalvalue = 0.0

    for item in arr:

        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
            knapsack.append(item)

        else:
            fraction=W / item.weight
            finalvalue += item.profit * W / item.weight
            item.fract=fraction
            knapsack.append(item)
            break

    return finalvalue,knapsack


def main():
    # W = 50
    # arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    
    W = int(input("Enter the knapsack weight (W): "))
    num_items = int(input("Enter the number of items: "))
    
    arr = []
    for i in range(num_items):
        name="item "+str(i+1)
        profit = int(input(f"Enter the profit for item {i+1}: "))
        weight = int(input(f"Enter the weight for item {i+1}: "))
        arr.append(Item(name,profit, weight))
    
    max_val,knapsack = fractionalKnapsack(W, arr)
    print(f"Total value of the knapsack: {max_val}")
    
    for item in knapsack:
        if item.fract==0:
            print(f"{item.name} - 1.00")
        else:
            print(f"{item.name} - {item.fract:.2f}")

if __name__ == "__main__":
    main()
