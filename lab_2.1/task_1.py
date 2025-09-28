text = input("Введите текст: ")

words = []
word = ""
i = 0
while i < len(text):
    if text[i] != " " and text[i] != "\n":
        word += text[i]
    else:
        if word != "":
            words.append(word)
            word = ""
    i += 1
if word != "":
    words.append(word)

word_count = {}
for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

unique_words = set()
for w in words:
    unique_words.add(w)

print("Словарь слов и их количества:")
print(word_count)
print("Количество уникальных слов:", len(unique_words))
