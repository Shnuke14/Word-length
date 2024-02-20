## Произвольное предложение
sentence = "the quick brown fox jumps over the lazy dog"
## Делим на слова
words = sentence.split()
## Создание пустого массива с длиной слов
word_lengths = []
## Цикл, если слово не "the", то он добавляет длину слова в массив
for word in words:
  if word != "the":
    word_lengths.append(len(word))

## Выведем слова и их длины
print(words)
print(word_lengths)