import random
import time
from dual_pivot import dualpivot


sizes = [1000, 10000, 50000, 100000, 500000, 1000000]
for size in sizes:
    random.seed(1)
    data = [random.randint(0, 10 ** 6) for _ in range(size)]
    start_time = time.time()
    sorted_data = dualpivot(data)
    end_time = time.time()
    print(f"Розмір: {size}, Час виконання: {end_time - start_time:.4f} сек")