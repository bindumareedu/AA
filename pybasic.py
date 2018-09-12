def BinarySearch(arr, key, lo, hi):
    if (hi < lo):
        return -1
    mid = lo + hi / 2
    if (key == arr[mid]):
        return mid
    if (key < arr[mid]):
        return BinarySearch(arr, key, lo, mid)
    else:
        return BinarySearch(arr, key, mid + 1, hi)


# MAIN CODE

arr = [3, 6, 9, 10, 15, 80, 45, 121, 150, 280, 200, 250, 300,350]
key = 280;
lo = 0;
hi = len(arr)
BinarySearch(arr, key, lo, hi)
print('mid');
