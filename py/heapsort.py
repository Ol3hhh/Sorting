data = [1, 16, 8, 14, 20, 1, 26]

def make_tree(data, i, bound):
    while 2 * i + 1 < bound:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = left

        if right < bound and data[right] > data[left]:
            largest = right

        if data[i] >= data[largest]:
            break

        data[i], data[largest] = data[largest], data[i]
        i = largest

def heapsort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        make_tree(data, i, n)

    for i in range(n - 1, 0, -1):
        if data[0] != data[i]:
            data[i], data[0] = data[0], data[i]
        make_tree(data, 0, i)

    return data

print(heapsort(data))
