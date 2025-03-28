def dualpivot(data):
    if len(data) <= 1:
        return data
    pivot1 = data[-1]
    pivot2 = data[0]
    if pivot1 > pivot2:
        pivot1, pivot2 = pivot2, pivot1
    left = [x for x in data[1:-1] if x < pivot1]
    center = [x for x in data[1:-1] if pivot1 <= x <= pivot2]
    right = [x for x in data[1:-1] if x > pivot2]
    return dualpivot(left) + [pivot1] + dualpivot(center) + [pivot2] + dualpivot(right)
data = list(range(1, 13))[::-1]
print(data)
print(dualpivot(data))
