from multiprocessing import Pool

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

def parallel_heapify(data, start_index, end_index):
    for i in range(start_index, end_index):
        make_tree(data, i, len(data))

def mheapsort(data):
    n = len(data)

    num_workers = 4
    chunk_size = n // num_workers

    with Pool(num_workers) as pool:
        pool.starmap(parallel_heapify, [(data, i * chunk_size, (i + 1) * chunk_size) for i in range(num_workers)])

    for i in range(n // 2 - 1, -1, -1):
        make_tree(data, i, n)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        make_tree(data, 0, i)

    return data


