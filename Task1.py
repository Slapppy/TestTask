def find_sum(N, M):
    digits = list(range(1, N + 1))
    operators = ["+"] * (N - 1)

    for i in range(2 ** (N - 1)):
        op_bits = bin(i)[2:].zfill(N - 1)
        op_sequence = [operators[j] if op_bits[j] == "0" else "" for j in range(N - 1)]
        expression = "".join([str(d) + op for d, op in zip(digits, op_sequence)]) + str(digits[-1])
        if eval(expression) == M:
            return f'{expression}={M}'
    return None


n, m = map(int, input().split())
# Примеры использования
print(find_sum(n, m))

