def quick_sort(words):
    if len(words) <= 1:
        return words

    pivot = words[0]
    pivot_len = len(pivot)

    left = []
    right = []
    for w in words[1:]:
        if len(w) < pivot_len:
            left.append(w)
        if len(w) > pivot_len:
            right.append(w)

    middle = []
    for w in words:
        if len(w) == pivot_len:
            middle.append(w)

    return quick_sort(left) + middle + quick_sort(right)


def max_word_chain(filename):
    words = []
    with open(filename, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            words.append(f.readline().strip())
    word_set = set(words)
    dp = {}

    words = quick_sort(words)

    max_chain = 1
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            shorter = word[:i] + word[i + 1 :]
            if shorter in word_set:
                if dp[word] < dp[shorter] + 1:
                    dp[word] = dp[shorter] + 1
        if dp[word] > max_chain:
            max_chain = dp[word]

    with open("wchain.out", "w") as f:
        f.write(str(max_chain) + "\n")
    return max_chain


result = max_word_chain("wchain.in.txt")
print(result)
