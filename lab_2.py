# В3 Р3
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
    max_possible = (free_sections[-1] + free_sections[0]) // (c - 1)
    while max_possible >= 1:
        a = 0
        counter = 1
        for j in range(1, len(free_sections)):
            if free_sections[j] - free_sections[a] >= max_possible:
                a = j
                counter += 1
        if counter < c:
            max_possible -= 1
        else:
            return max_possible


print(min_distance([1, 2, 8, 4, 9], 3))
