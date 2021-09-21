HELP = """
help - напечатать справку по программе
add - добавить задачу в список
show - просмотреть все добавленные задачи
exit - выход из программы """

tasks = {}

run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        date = input('Введите дату для отображения списка задач: ')
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print('Такой даты нет')
    elif command == 'add':
        date = input('Введите дату для добавления задачи: ')
        task = input('Введите название задачи: ')
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = [task]
        print('Задача', task, 'добавлена на дату', date)
    elif command == 'exit':
        break
    else:
        print('Неизвестная команда')
        break

print('Спасибо за использование программы. До свидания.')
