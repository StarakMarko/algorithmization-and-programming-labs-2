def counting_sort(words):
    if not words:
        return []
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)

    count = [[] for _ in range(max_len + 1)]

    for word in words:
        count[len(word)].append(word)

    sorted_words = []
    for bucket in count:
        sorted_words.extend(bucket)

    return sorted_words


def max_word_chain(filename):
    words = []
    with open(filename, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            words.append(f.readline().strip())
    word_set = set(words)
    dp = {}

    words = counting_sort(words)

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
