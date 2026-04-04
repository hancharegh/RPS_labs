def shaker_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        swapped = False

        # Проход слева направо
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        right -= 1

        # Проход справа налево
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        left += 1

        if not swapped:
            break

    return arr
