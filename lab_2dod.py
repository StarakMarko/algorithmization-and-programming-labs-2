# В3 Р3
with open("numbers.txt", "r") as file:
    lst = [int(line.strip()) for line in file]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


def min_distance(free_sections, c):
    merge_sort(free_sections)
    left = 0
    right = (free_sections[-1] + free_sections[0]) // 2
    best_dist = 0
    co = 0
    while left <= right:
        co += 1
        mid = (left + right) // 2
        a = 0
        counter = 1
        for j in range(1, len(free_sections)):

            if free_sections[j] - free_sections[a] >= mid:
                a = j
                counter += 1
        if counter >= c:
            best_dist = mid
            left = mid + 1
        else:
            right = mid - 1
    print(co)
    return best_dist


print(min_distance(lst, 10000))
