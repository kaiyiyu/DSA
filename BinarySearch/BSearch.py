# Adapted from Grokking Algorithms

def binary_search(list, item):
    low = 0
    high = len(list) - 1 
    steps = 0   # track number of steps
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
    
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
        
        steps += 1
    
    print(f"The number of steps to find the number is {steps}.")
        
    return None

if __name__ == "__main__":   
    my_list = [1, 3, 5, 7, 9]
    b1 = binary_search(my_list, 3) # => 1
    b2 = binary_search(my_list, -1) # => None
    
    print(f"The number is {b1}.")
    print(f"The number is {b2}.")
    