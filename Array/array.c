#include <stdio.h>

#define MAX_SIZE 100  // Maximum size of the array

// Function to insert an element at the specified index
void insert(int array[], int *length, int index, int element) {
    if (*length >= MAX_SIZE) {
        printf("Array is full. Insertion failed.\n");
        return;
    }
    if (index < 0 || index > *length) {
        printf("Invalid index. Insertion failed.\n");
        return;
    }

    // Shift elements to the right to make space for the new element
    for (int i = *length; i > index; i--) {
        array[i] = array[i - 1];
    }

    // Insert the new element at the specified index
    array[index] = element;
    (*length)++;
}

// Function to delete an element at the specified index
void delete(int array[], int *length, int index) {
    if (index < 0 || index >= *length) {
        printf("Invalid index. Deletion failed.\n");
        return;
    }

    // Shift elements to the left to remove the element at the specified index
    for (int i = index; i < *length - 1; i++) {
        array[i] = array[i + 1];
    }

    (*length)--;
}

// Function to search for an element in the array
int search(int array[], int length, int element) {
    for (int i = 0; i < length; i++) {
        if (array[i] == element) {
            return i;  // Return the index of the element if found
        }
    }
    return -1;  // Return -1 if the element is not found
}

int main() {
    int my_array[MAX_SIZE] = {1, 2, 3, 4, 5};
    int length = 5;  // Current length of the array

    // Insert an element at index 2
    insert(my_array, &length, 2, 10);
    printf("Array after insertion: ");
    for (int i = 0; i < length; i++) {
        printf("%d ", my_array[i]);
    }
    printf("\n");

    // Delete the element at index 3
    delete(my_array, &length, 3);
    printf("Array after deletion: ");
    for (int i = 0; i < length; i++) {
        printf("%d ", my_array[i]);
    }
    printf("\n");

    // Search for element 3
    int index = search(my_array, length, 3);
    if (index != -1) {
        printf("Element 3 found at index %d\n", index);
    } else {
        printf("Element 3 not found\n");
    }

    return 0;
}