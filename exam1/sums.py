array_to_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def recursive_array_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_array_sum(arr[1:])

def iterative_array_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print(f"Recursive sum: {recursive_array_sum(array_to_sum)}")
print(f"Iterative sum: {iterative_array_sum(array_to_sum)}")