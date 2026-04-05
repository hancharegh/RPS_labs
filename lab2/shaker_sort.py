def shaker_sort(arr):
    arr = arr.copy()
    left = 0
    right = len(arr) - 1

    while left <= right:
        swapped = False

        # проход слева направо
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        right -= 1

        if not swapped:
            break

        swapped = False

        # проход справа налево
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        left += 1

        if not swapped:
            break

    return arr
