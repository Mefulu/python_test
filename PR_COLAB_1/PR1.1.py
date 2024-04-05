def rev_and_res(words):
  # Разворачиваем список.
  rev_words = words[::-1]

  # Преобразуем список в строку, разделённую пробелами.
  res_words = " ".join(rev_words)

  # Удаляем пробел в конце строки.
  return res_words.rstrip()

# Пример использования.
words = ["language!", "programming", "Python", "the", "love", "I"]
rev_and_res = rev_and_res(words)
print(rev_and_res)
