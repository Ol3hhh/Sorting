def insertion_sort(data):
    for i in range(1, len(data)):
        current_value = data[i]
        j = i - 1
        while j >= 0 and data[j] > current_value:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current_value

    return data



