import random
import time
import sys
import pandas as pd
from mutli_heapsort import mheapsort
from dual_pivot import dualpivot  
from heapsort import heapsort
from timsort import timsort


sys.setrecursionlimit(10**6)

def generate_partial_sorted_list(size, sorted_ratio=0.25, min_val=0, max_val=10 ** 6, reverse=False):
    data = [random.randint(min_val, max_val) for _ in range(size)]
    split_index = int(size * sorted_ratio)
    sorted_part = sorted(data[:split_index], reverse=reverse)
    unsorted_part = data[split_index:]
    random.shuffle(unsorted_part)
    return sorted_part + unsorted_part

def expect_sort_result(sort_func, data, ref_value, sort_name):
    sorted_data = sort_func(data.copy())
    if sorted_data != ref_value:
        print(f"{sort_name} failed: expected {ref_value[:10]}..., but got {sorted_data[:10]}...")
        sys.exit(1)

def benchmark_sorting_algorithms():
    sizes = [1000, 10000]
    sort_functions = {
        "mheapsort": mheapsort,
    }
    sorted_ratios = [0.25, 0.50, 0.75, 0.95, 0.99, 1.0]

    results = []
    log_buffer = []

    for iteration in range(100):  
        log_buffer.append(f"Iteration {iteration + 1}/10")
        for size in sizes:
            for sort_name, sort_func in sort_functions.items():
                random.seed(10)
                data = [random.randint(0, 10 ** 6) for _ in range(size)]
                ref_value = sorted(data)
                log_buffer.append(f"Running {sort_name} on random data of size {size}...")
                start_time = time.time()
                sorted_data = sort_func(data.copy())
                end_time = time.time()
                expect_sort_result(sort_func, data, ref_value, sort_name)
                results.append([sort_name, size, "Random", end_time - start_time])
                log_buffer.append(f"{sort_name} completed in {end_time - start_time:.4f} seconds.")

            for ratio in sorted_ratios:
                for sort_name, sort_func in sort_functions.items():
                    random.seed(10)
                    data = generate_partial_sorted_list(size, sorted_ratio=ratio)
                    ref_value = sorted(data)
                    log_buffer.append(f"Running {sort_name} on {float(ratio * 100)}% sorted data of size {size}...")
                    start_time = time.time()
                    sorted_data = sort_func(data.copy())
                    end_time = time.time()
                    expect_sort_result(sort_func, data, ref_value, sort_name)
                    results.append([sort_name, size, f"Sorted {float(ratio * 100)}%", end_time - start_time])
                    log_buffer.append(f"{sort_name} completed in {end_time - start_time:.4f} seconds.")

            for sort_name, sort_func in sort_functions.items():
                random.seed(10)
                data = sorted([random.randint(0, 10 ** 6) for _ in range(size)], reverse=True)
                ref_value = sorted(data)
                log_buffer.append(f"Running {sort_name} on reverse sorted data of size {size}...")
                start_time = time.time()
                sorted_data = sort_func(data.copy())
                end_time = time.time()
                expect_sort_result(sort_func, data, ref_value, sort_name)
                results.append([sort_name, size, "Reverse Sorted", end_time - start_time])
                log_buffer.append(f"{sort_name} completed in {end_time - start_time:.4f} seconds.")

        print("\n".join(log_buffer))
        log_buffer.clear()

    df = pd.DataFrame(results, columns=["Algorithm", "Size", "Data Type", "Time (sec)"])
    df = df.sort_values(by=["Algorithm", "Size", "Data Type"])
    df.to_excel("mheapsort_results.xlsx", index=False)

if __name__ == "__main__":
    benchmark_sorting_algorithms()
