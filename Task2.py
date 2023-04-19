def find_max_monotonic_subarray(arr):
    n = len(arr)
    L = [1] * n

    # Вычисляем длины максимальных монотонных подотрезков
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            L[i] = L[i-1] + 1

    # Находим максимальную длину и её индекс
    max_len = max(L)
    max_idx = L.index(max_len)

    # Находим индекс начала максимального монотонного подотрезка
    start_idx = max_idx - max_len + 1

    return start_idx, max_idx


arr = list(map(int, input().split(',')))

print(find_max_monotonic_subarray(arr))

