def array_sum(arr, n):
    if n <= 0:
        return 0
    else:
        return arr[n - 1] + array_sum(arr, n - 1)

print(array_sum([1, 2, 3, 4, 5], 5))


def n_choose_k(n, k):
    if k == 0 or k == n:
        return 1
    return n_choose_k(n - 1, k - 1) + n_choose_k(n - 1, k)

print(n_choose_k(5, 2))

