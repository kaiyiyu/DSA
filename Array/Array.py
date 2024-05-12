# Python program to demonstrate arrays

"""
Things to note when implementing in Python:
1. No need to indicate size of array/dynamic sizing
2. Implemented as lists that can hold different data types    
"""

# Create empty array
new_array = []

# Add values 
new_array.append("Hello")
new_array.append(1)
new_array.append(3.14)
new_array.append(True)

# Access elements
print(new_array[2])
print(new_array[0]) 

# Update elements
new_array[3] = False
print(new_array)    # Output: ['Hello', 1, False]

# Delete elements by index
del new_array[2]    # 
print(new_array)   # Output: ['Hello', 1, False]

# Remove first occurence in array
new_array.remove("Hello")
print(new_array)    # Output: [1, False]

# Inserting an element at specific index
new_array.insert(0, "Goodbye",)  # At index 0 insert "Goodbye"
print(new_array) # Output: ["Goodbye", 1, False]


for i in new_array:
    print(i)

test = [0, 1, 2, 3, 4, 0, 5, 6, 7, 0]
test1 = [x for x in test if x != 0]
print(test)
print(test1)

