import random
import time

def quickSort(data):
    if len(data) <= 1:
        return data

    pivot = data[-1]
    left = [x for x in data[:-1] if x <= pivot]
    right = [x for x in data[:-1] if x > pivot]

    return quickSort(left) + [pivot] + quickSort(right)


sizes = [1000, 10000, 50000, 100000, 500000, 1000_000]
for size in sizes:
    random.seed(1)
    data = [random.randint(0, 10 ** 6) for _ in range(size)]
    start_time = time.time()
    sorted_data = quickSort(data)
    end_time = time.time()

    print(f"szie: {size}, time: {end_time - start_time:.4f} seconds")

