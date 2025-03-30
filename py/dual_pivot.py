def dualpivot(data, low=0, high=None):
    if high is None:
        high = len(data) - 1

    if low >= high:
        return

    if data[low] > data[high]:
        data[low], data[high] = data[high], data[low]

    pivot1, pivot2 = data[low], data[high]
    left, right = low + 1, high - 1
    i = left

    while i <= right:
        if data[i] < pivot1:
            data[i], data[left] = data[left], data[i]
            left += 1
        elif data[i] > pivot2:
            while i < right and data[right] > pivot2:
                right -= 1
            data[i], data[right] = data[right], data[i]
            right -= 1
            if data[i] < pivot1:
                data[i], data[left] = data[left], data[i]
                left += 1
        i += 1

    left -= 1
    right += 1
    data[low], data[left] = data[left], data[low]
    data[high], data[right] = data[right], data[high]

    dualpivot(data, low, left - 1)
    dualpivot(data, left + 1, right - 1)
    dualpivot(data, right + 1, high)

    return data