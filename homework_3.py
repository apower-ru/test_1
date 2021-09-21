a = ['python', 'c++', 'c', 'scala', 'java']
b = input('Введите букву: ')


def count_letter(word_list, letter):
    count = 0
    for word in word_list:
        if letter in word:
            count += 1
    return count


print('Количество слов с буквой -', count_letter(a, b))
