def calcMinRun(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r

def merge(data, left, mid, right):
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if data[i] <= data[j]:
            i += 1
        else:
            value = data[j]
            k = j
            while k > i:
                data[k] = data[k - 1]
                k -= 1
            data[i] = value
            i += 1
            j += 1

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

        if end - start + 1 >= minrun:
            runs.append((start, end))
            i = end + 1
        else:
            end = start
            while end + 1 < n and data[end] >= data[end + 1]:
                end += 1

            if end - start + 1 >= minrun:
                data[start:end + 1] = data[start:end + 1][::-1]
                runs.append((start, end))
                i = end + 1
            else:
                end = min(start + minrun - 1, n - 1)
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

    print("Sorted Array:")
    print(data)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 4, 21, 5, 4, 2, 1, 7, 23, 19, 3, 1, 16]

    print("Given Array:")
    print(data)

    timsort(data)
