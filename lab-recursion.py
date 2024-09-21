# Let's split some arrays right down the middle!
def recursive_binary_search(arr, target, low, high):

    # Base case: no more elements to search
    if low > high:
        return -1 # 404 number not found :-(

    # Calculate the middle index
    mid = (low + high) // 2

    # Base case: if middle element is the target
    if arr[mid] == target:
        return mid  # We did it! :-)

    # Split down the middle; search in the left half
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)

    # Otherwise, search in the right half
    else:
        return recursive_binary_search(arr, target, mid + 1, high)

# We could read in user input in a while loop, but for now we'll hardcode the values
nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 5

# Now let's do the binary search
result = recursive_binary_search(nums, target, 0, len(nums) - 1)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")

# Because strings can also be sorted, we can search an array of string values too
names = ["Adrian", "Bryan", "Eddie", "Matt", "Jadon", "Jason", "Taoufik", "Vidiya" "Yushi"]
target = "Taoufik"

# Now let's search for you among the students
result = recursive_binary_search(names, target, 0, len(names) - 1)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")

