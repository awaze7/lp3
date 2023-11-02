class Item:
    def __init__(self, value, weight, index):
        self.value = value
        self.weight = weight
        self.index = index

def knapsack_branch_and_bound(values, weights, capacity):
    items = []

    for i in range(len(values)):
        value = values[i]
        weight = weights[i]
        item = Item(value, weight, i)
        items.append(item)

    items.sort(key=lambda x: x.value/x.weight, reverse=True)  # Sort items by value/weight ratio (desc)

    def get_bound(current, remaining_capacity, i):
        # Calculate the bound for the current node
        bound = current
        total_weight = 0
        while i< len(items):
            if items[i].weight<=remaining_capacity:
                bound += items[i].value
                remaining_capacity-=items[i].weight
            else:
                bound+=items[i].value* (remaining_capacity)/items[i].weight
                break
                
        return bound

    def branch_and_bound(i, current_value, current_weight, selected_items):
        nonlocal max_value, result_items

        if current_weight > capacity or i == len(items):
            return

        if current_value > max_value:
            max_value = current_value
            result_items = selected_items.copy()

        bound = get_bound(current_value, capacity - current_weight, i)

        if bound > max_value:
            selected_items.append(items[i].index) #stores the original index of items
            branch_and_bound(i + 1, current_value + items[i].value, current_weight + items[i].weight, selected_items)
            selected_items.pop()
            branch_and_bound(i + 1, current_value, current_weight, selected_items)

    max_value = 0
    result_items = []
    branch_and_bound(0, 0, 0, [])

    return max_value, result_items

# Example usage
if __name__ == "__main__":
#     values = [10, 40, 30, 50]
#     weights = [5, 4, 6, 3]
#     capacity = 10
    
    capacity=int(input("Enter the weight capacity of Knapsack:"))
    n=int(input("Enter the number of items:"))
    values=[]
    weights=[]
    
    for i in range(n):
        values.append(int(input(f"Enter the value of item {i+1}:")))
        weights.append(int(input(f"Enter the weight of item {i+1}:")))
        
    # Solve the 0-1 Knapsack Problem using Branch and Bound
    max_value, selected_items = knapsack_branch_and_bound(values, weights, capacity)

    
    selected_items
    print("Selected items:")
    for i in selected_items:
        print(f"Item {i + 1} (Value: {values[i]}, Weight: {weights[i]})")
    print(f"\nMaximum value in the knapsack: {max_value}")
