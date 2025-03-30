
def calcMinRun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r + 32

def merge(data, left, mid, right):
    left_part = data[left:mid + 1]
    right_part = data[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            data[k] = left_part[i]
            i += 1
        else:
            data[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        data[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        data[k] = right_part[j]
        j += 1
        k += 1

def insertion_sort(data, left, right):
    for i in range(left + 1, right + 1):
        current_value = data[i]
        j = i - 1
        while j >= left and data[j] > current_value:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current_value

def adapt_runs(data, n, minrun):
    i = 0
    runs = []

    while i < n:
        start = i
        end = i

        while end + 1 < n and data[end] <= data[end + 1]:
            end += 1

        if end == start:
            while end + 1 < n and data[end] >= data[end + 1]:
                end += 1
            data[start:end + 1] = reversed(data[start:end + 1])

        run_size = end - start + 1
        if run_size < minrun:
            end = min(start + minrun - 1, n - 1)
            insertion_sort(data, start, end)

        runs.append((start, end))
        i = end + 1

    return runs

def timsort(data):
    n = len(data)
    minrun = calcMinRun(n)
    runs = adapt_runs(data, n, minrun)

    for run in runs:
        insertion_sort(data, run[0], run[1])

    while len(runs) > 1:
        merged_runs = []
        i = 0

        while i < len(runs) - 1:
            left_run = runs[i]
            right_run = runs[i + 1]
            merge(data, left_run[0], left_run[1], right_run[1])
            merged_runs.append((left_run[0], right_run[1]))
            i += 2

        if i < len(runs):
            merged_runs.append(runs[i])

        runs = merged_runs

    return data

