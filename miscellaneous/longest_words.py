def longest_word(apple):
    with open("apple.txt", 'r') as infile:
              w = infile.read().split()
    max_len = len(max(w, key=len))
    return [word for word in w if len(word) == max_len]

print(longest_word('apple.txt'))