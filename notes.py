with open('D:\\notes.txt', 'r', encoding='cp1251') as inf:
    data = inf.read().strip().split('\n')
    notes = {}
    for i in data:
        i = (i.strip().split('--'))
        notes[i[0]] = i[1]
    my_input = input('Что надо найти или "enter" для записи: ').strip().lower()
    if my_input in notes.keys():
        print('ОТВЕТ:', notes[my_input])
    elif my_input == '':
        out = input('Название заметки: ').lower()
        if out in notes.keys():
            print('Есть такая -', notes[out])
            text = input('Изменить на (или "enter" для выхода): ')
            if text != '':
                notes[out] = text
        else:
            text = input('Заметка: ')
            if text != '':
                notes[out] = text
    else:
        print('похожие записи')
with open('D:\\notes.txt', 'w') as ouf:
    for key, value in notes.items():
        print(key + '--' + value, file=ouf)


# for key, value in notes.items(): print(key, ':', value)
# for key in notes.keys(): print(key)
# for value in notes.values(): print(value)
# with open(path, 'rb') as f:
#   contents = f.read()
# with open('D:\\notes.txt', 'r', encoding='utf-8') as inf:
#     data = inf.read().strip().split('\n')
# with open(filename, encoding=encoding) as file:
    # encoding='cp1251'