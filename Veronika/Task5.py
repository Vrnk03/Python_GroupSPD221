def func(sentence: str) -> int:
    words_list = sentence.split()
    shortest = min(len(word) for word in words_list)
    return shortest

print(func('Name of dog is Tom'))
print(func('Dog Tom'))
