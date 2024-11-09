import random

# Bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)

    # Iterate through the array
    for i in range(n):

        if(n <= 10):
            print(f"Pass {i + 1}: {arr}")

        # Early exit flag for efficiency
        swapped = False
        
        # Bubble sort pass
        for j in range(0, n - i - 1):

            # Check values and swap if necessary
            if arr[j] > arr[j + 1]:

                # Move the larger element to the right
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps happened, break out because the array is already sorted
        if not swapped:
            break

    return arr

def main():

    array_size = int(input("Enter the size of the array (if size <= 10 we'll display each pass): "))

    # Generate a list of random numbers for sorting
    pre_sort = [random.randint(0, array_size) for i in range(array_size)]
    print("\nList before sorting:\n", pre_sort, "\n")

    # Print the sorted list
    print("\nList after sorting:\n", bubble_sort(pre_sort))

if __name__ == "__main__":
    main()