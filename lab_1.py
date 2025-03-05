# В3 P3

lst = [1, 3, 5, 4, 2, 8, 3, 7]


def peak_sequence(lst):
    max_length = 0
    i = 1
    for i in range(1, len(lst) - 1):
        if lst[i - 1] < lst[i] and lst[i] > lst[i + 1]:
            left_index = i - 1
            left_len = 1
            right_index = i + 1
            right_len = 1
            while left_index > 0 and lst[left_index - 1] < lst[left_index]:
                left_index -= 1
                left_len += 1
            while (
                right_index < len(lst) - 1 and lst[right_index] > lst[right_index + 1]
            ):
                right_index += 1
                right_len += 1
            length = 0
            if left_len > right_len:
                length = right_len * 2 + 1
            else:
                length = left_len * 2 + 1
            if max_length < length:
                max_length = length
    return max_length


print(peak_sequence(lst))
