# Adapted from Grokking Algorithms

# method to find smallest value
def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
            
    return smallest_index

# selection sort
def selectionSort(array):
    new_array = []
    copied_array = array.copy() # deep copy
    for i in range(len(copied_array)):
        smallest_value = findSmallest(copied_array)
        new_array.append(copied_array[smallest_value])
        copied_array.pop(smallest_value)

    return new_array

if __name__ == "__main__":
    num_array = [5, 3, 6, 2, 10, 4, 3]
    
    sorted_array = selectionSort(num_array)
    print(sorted_array)