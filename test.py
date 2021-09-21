# n = int(input().strip())  #strip() - убрать все служебные символы
# if 1 <= n <= 100:
#     if n % 2 == 0 and (2 <= n < 5 or n > 20):
#         print('Not Weird')
#     else:
#         print('Weird')
#
# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
#
# print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))

# n = int(input().strip())
# i = 0
# if 1 <= n <= 20:
#     while n > i:
#         print(i * i)
#         i += 1

# year = int(input())

# def is_leap(year):
#     leap = False
#     if year % 400 == 0:
#         leap = True
#     elif year % 100 == 0:
#         leap = False
#     elif year % 4 == 0:
#         leap = True
#     return leap

# def is_leap(year):
#  return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

# print(is_leap(year))

# X = int(input())
# H = int(input())
# M = int(input())
# X += (H * 60 + M)
# print(X // 60, '\n', X % 60, sep='')

# A = int(input())
# B = int(input())
# H = int(input())
# if A <= H <= B:
#     print("Это нормально")
# elif H < A:
#     print("Недосып")
# elif H > B:
#     print("Пересып")

# a = int(input())
# b = int(input())
# x = int(input())
# print(("Недосып", "Это нормально", "Пересып")[(x > b) - (x < a) + 1])

# a, b, h = (int(input()) for _ in range(3))
# print('Это нормально'*(a <= h <= b) + 'Недосып'*(h < a) + 'Пересып'*(h > b))

# n = int(input())
# if 1900 <= n <= 3000:
#     if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#         print('Високосный')
#     else:
#         print('Обычный')

# print("123" + "42")
# print(repr('123' + '42'))

# a, b, c = int(input()), int(input()), int(input())
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and b + c > a:
#     p = (a + b + c) / 2
#     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(s)
# else:
#     print('Не выполнено неравенство треугольника')

# x = int(input())
# if -15 < x <= 12 or 14 < x < 17 or x >= 19:
#     print('True')
# else:
#     print('False')


# a = float(input())
# b = float(input())
# c = input()
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == 'pow':
#     print(a ** b)
# elif b != 0:
#     if c == '/':
#         print(a / b)
#     elif c == 'mod'::
#         print(a % b)
#     elif c == 'div':
#         print(a // b)
# else:
#     print('Деление на 0!')

# share = input()
# a = float(input())
# if share == 'круг':
#     print(3.14 * a**2)
# elif share == 'прямоугольник':
#     b = float(input())
#     print(a * b)
# elif share == 'треугольник':
#     b, c = float(input()), float(input())
#     p = (a + b + c) / 2
#     print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

# a, b, c = int(input()), int(input()), int(input())
# max = c
# min = c
# mean = c
# if a >= b and a >= c:
#     max = a
# elif b >= a and b >= c:
#     max = b
# if a <= b and a <= c:
#     min = a
# elif b <= a and b <= c:
#     min = b
# if max == c and min == b or max == b and min == c:
#     mean = a
# elif max == c and min == a or max == a and min == c:
#     mean = b
# print(max, min, mean, sep="\n")

# a, b, c = int(input()), int(input()), int(input())
# if a < b:
#     a, b = b, a
# if a < c:
#     a, c = c, a
# if b < c:
#     c, b = b, c
# print(a, c, b, sep='\n')


# number = int(input())
# if 0 <= number <= 1000:
#     if number % 100 in [11, 12, 13, 14] or number % 10 in [0, 5, 6, 7, 8, 9]:
#         print(number, 'программистов')
#     elif number % 10 == 1:
#         print(number, 'программист')
#     elif number % 10 in [2, 3, 4]:
#         print(number, 'программиста')

# a, b, c, d, e, f = input()
# if int(a) + int(b) + int(c) == int(d) + int(e) + int(f):
#     print('Счастливый')
# else:
#     print('Обычный')
#
# number = input()
# answer = { True: "Счастливый", False: "Обычный" }
# leftSum = 0
# for i in range(0, 3):
#     leftSum += int(number[i])
# rightSum = 0
# for i in range(3, 6):
#     rightSum += int(number[i])
# print( answer[ leftSum == rightSum] )

# ans = {False: 'Счастливый', True : 'Обычный'}
# b,c,d,e,f,g = (int(n) for n in input())
# print(ans[bool((b+c+d)-(e+f+g))])


# i, s = 1, 0
# while i != 0:
#     i = int(input())
#     s += i
# print(s)

# a, b = int(input()), int(input())
# i = 1
# while not(i % a == 0 and i % b == 0):
#     i += 1
# print(i)

# a = int(input())
# b = int(input())
# d = a
# while d % b:
#     d += a
# print(d)


# s = ''
# while True:
#     i = int(input())
#     if i < 10:
#         continue
#     elif i > 100:
#         break
#     s += str(i) + '\n'
# print(s)


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# for x in range(c, d + 1):
#     print('\t' + str(x), end='')
# print()
# for i in range(a, b + 1):
#     print(i, end='\t')
#     for j in range(c, d + 1):
#         print(i * j, end='\t')
#     print()

# a,b,c,d = ( int(input()) for i in range(4))
# print('\t', *range(c, d+1), sep='\t')
# [ print(*[i, *range(i*c, i*d+1, i)], sep='\t') for i in range(a, b+1) ]


# a, b = (int(input()) for i in range(2))  # ввод двух чисел последовательно
# print(a)
# print(b)

# a, b = (int(i) for i in input().split())  # ввод чисел в одной строке
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     s += i
# print(s)

# a, b = (int(input()) for i in range(2))
# s, n = 0, 0
# if a % 3 != 0:
#     a += 1
# if a % 3 != 0:
#     a += 1
# for i in range(a, b + 1, 3):
#     s += i
#     n += 1
# print(s / n)

"""
a, b = int(input()), int(input())
a += -a % 3
b -= b % 3
print((a + b) / 2)
во первых мы находим ближайшие к границам отрезка числа a и b, которые делятся на 3.
Я не знаю, как это можно доказать математически, у нас есть числа -3,0,3,6,9,12 (первый пример [-5,12])
- и мы должны найти их середину. Стоит отметить, что в этом списке нет повторов и между числами одинаковое
расстояние => мы должны найти середину этого списка. Что можно сделать несколькими способами. Например сложить
все числа и разделить на их количество или поступить так же, но уже с двумя границами (a и b), что будет явно быстрее.
"""

# genome = 'ATTG'  # поочередное перечисление всех символов строки
# for c in genome:
#     print(c)

# genome = input()
# cnt = 0
# for nukl in genome:
#    if nukl == 'C':
#        cnt += 1
# print(cnt)

# genome = input()  # То же что и выше
# print(genome.count('C'))

# line = input()
# count = 0
# for a in line.lower():
#     # if a != 'g' and a != 'c':
#     if a not in ('g', 'c'):
#         continue
#     count += 1
# print(count / len(line) * 100)
#
# s = input().upper()
# print((s.count('G') + s.count('C'))/len(s) * 100)

# s = 'abcdefghijk'
# print(s[3:6], s[:6], s[3:], s[::-1], s[-3:], s[:-6],s[-1:-10:-2])

# s = input()
# my_s = s + '*'
# a, b, p, count_a, count = '', '', '', 0, 0
# while len(s) > count:
#     a, b = my_s[count], my_s[count + 1]
#     count += 1
#     count_a += 1
#     if a == b:
#         continue
#     p += a + str(count_a)
#     count_a = 0
# print(p)
#
# genome = input() + ' '
# s = 0
# n = genome[0]         # n = первый элемент в повторяющейся последовательности, для первого элемента строки это верно.
# for i in genome:    # текущий элемент всегда i
#     if n != i:      # в цикл попадаем, когда первый элемент повторяющихся элементов не совпадёт со следующим элементом
#         print(n + str(s), end='')
#         s = 0       # инициализируем длину для новой повторяющейся последовательности = 0
#         n = i       # новая последовательность начинается с нового элемента, запишем его в n
#     s += 1  # мы сдвинулись на 1 элемент, поэтому увеличиваем последовательность элементов на 1.

# list = [int(i) for i in input().split()]
# print(sum(list))
#
# a = [int(i) for i in input().split()]
# s = 0
# for i in a:
#     s += i
# print(s)


# list = [int(i) for i in input().split()]
# s = 0
# while len(list) > s:
#     if len(list) == 1:
#         a = list[0]
#     elif len(list) > s + 1:
#         a = list[s - 1] + list[s + 1]
#     else:
#         a = list[s - 1] + list[0]
#     print(a, end=' ')
#     s += 1

#
# arr = list(map(int, input().split()))
# print(*arr if len(arr) == 1 else [arr[i - 1] + arr[(i + 1) % len(arr)] for i in range(len(arr))])
#
# a=[int(i) for i in input().split()]
# if len(a)>1:
#     for i in range(len(a)):
#         print(a[i-1]+a[i+1-len(a)])
# else:
#     print(a[0])
#
# src = [int(i) for i in input().split()]
# if len(src) == 1:
#     print(src[0])
# else:
#     [print( src[i-1] + src[(i+1) % len(src)] ,end=' ') for i in range(len(src))]
#     # выражение src[(i+1) % len(src)] на выходе для src = [1, 3, 5, 6, 10] даст [3, 5, 6, 10, 1]
#     # потому, что (i+1) % len(src) даёт 1 2 3 4 0
#     # т.е. таким образом 0й элемент оказывается в конце списка (как будто повернули циферблат)
#     # таким образом если при обращении к i+1 случится выход за границу диапазона для последнего элемента
#     # то при обращении к (i+1) % len(src) элементу выхода не произойдет
#     # поэтому складывая -1й элемент с [(i+1) % len(src)]-тым элементом
#     # мы выполним условие найти сумму предыдущего и следующего элементов
#     # [print( src[(i+1) % len(src)]) for i in range(len(src))]
#
# x = [int(i) for i in input().split(' ')]  # создаем список, напр [1, 2, 3, 4, 5]
#
# if len(x) <= 1:
#     print(x[0])
# else:
#
#     y = [x[i - 1] for i in range(len(x))]  # массив перестановка вправо [5, 1, 2, 3, 4]
#     z = [x[i] for i in range(-len(x) + 1, 1)]  # массив перестановка влево [2, 3, 4, 5, 1]
#
#     for i in range(len(x)): print(y[i] + z[i], end=' ')  # теперь просто поэлементно сложить


# list = [int(i) for i in input().split()]
# list.sort()
# n = ''
# trigger = True
# for i in list:
#     if n == i and trigger:
#         print(i, end=' ')
#         trigger = False
#     if n != i:
#         trigger = True
#     n = i
#
#
# a, b = [int(i) for i in input().split()], []
# for i in a:
#     if a.count(i) > 1 and b.count(i) == 0:
#         b.append(i)
# for i in b:
#     print(i, end=" ")
#
# ls = [int(i) for i in input().split()]
# for i in set(ls):
#     if ls.count(i) > 1:
#         print(i, end=' ')
#
# a,b=[int(i) for i in input().split()],''
# a.sort()
# for i in range(len(a)-1):
#     if a[i]==a[i+1] and a[i]!=b:
#         print(a[i], end=' ')
#         b=a[i]
#
# str = [int(i) for i in input().split()]
# ans = []
# [ans.append(x) for x in str if x not in ans and str.count(x) > 1]
# print(*ans)


# n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин (строки, столбцы, кол-во мин)
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):  # перебираем кол-во мин
#     row, col = (int(i) - 1 for i in input().split())  # записываем строку и столбец одной мины при каждом проходе
#     a[row][col] = -1  # расставляем мины (записываем мину по координатам столбца и колонны)
# # дальше нам нужно заглянуть в каждую пустую ячейку, и находясь в ячейке пробежаться еще вокруг и поискать мины
# for i in range(n):  # перебираем строки
#     for j in range(m):   # перебираем столбцы
#         if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#             for di in range(-1, 2):  # перебираем соседние строки (просто цифры -1 0 1)
#                 for dj in range(-1, 2):  # перебираем соседние столбцы (просто цифры -1 0 1)
#                     ai = i + di   # координата по строке
#                     aj = j + dj   # координата по столбцу
#                     # (ai, aj)
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1: # проверка вхождения в диапазон и мин рядом
#                         a[i][j] += 1
#
# в поле 5х4 цикл пройдется 5 * 4 = 20 раз по ячейкам и, находясь в ячейке еще по 9(3*3) проходов вокруг.
# Всего будет 20*9=180 раз (или n*m*9 раз)
# # так же можно искать не пустые ячейки, а ячейки с миной (if a[i][j] == -1) и вокруг прибавлять единицу
# # код почти такой же, меняется последнее условие:
# '''
#                     if 0 <= ai < n and 0 <= aj < m:
#                         if a[ai][aj] != -1: # проверка, чтобы не увеличивать на 1 мину
#                             a[ai][aj] += 1
# '''
# # дальше просто заменяем -1 на "*" и 0 на "."
#
# вывод результата
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='\t')
#         elif a[i][j] == 0:
#             print('.', end='\t')
#         else:
#             print(a[i][j], end='\t')
#     print()

# b, c = 0, 0,
# while True:
#     a = int(input())
#     b += a * a
#     c += a
#     if c == 0:
#         break
# print(b)
#
# s=[int(input())]
# while sum(s)!=0: s.append(int(input()))
# print(sum([i**2 for i in s]))
#

# a = int(input())
# s = []
# i = 1
# while a > len(s):
#     for c in range(i):
#         s.append(i)
#     i += 1
# print(*s[:a])
#
# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])
#
# n = int(input())
# count = 0
# curr = 1
# for i in range(n):
#     print(curr, end=' ')
#     count += 1
#     if count == curr:
#         curr += 1
#         count = 0
#
# a = int(input())
# c = 0
# for i in range(a+1):
#     for j in range(i):
#         c += 1
#         print(i, end=' ')
#         if c < a + 1:
#             print(i)

# lst = [int(i) for i in input().split()]
# x = int(input())
# a, b = 0, 0
# if lst.count(x) > 0:
#     while lst.count(x) > b:
#         print(lst.index(x, a), end=' ')
#         a = lst.index(x, a) + 1
#         b += 1
# else:
#     print('Отсутствует')

# l = [int(i) for i in input().split()]
# x = int(input())
# if not x in l:
#     print('Отсутствует')
# for i in range(len(l)):
#     if l[i] == x:
#         print(i, end=' ')
#
# a = [int(i) for i in input().split()]
# b = int(input())
# if b in a:
#     while b in a:
#         print(a.index(b), end=' ')  # Первая строка выводит индекс первого числа, равного числу b, в списке
#         a[a.index(b)] = b + 1  # Вторая строка увеличивает на 1 значение числа с найденным индексом
# else:
#     print('Отсутствует')

#
# s = [[int(i) for i in input().split()]]
# a = input()
# while a != 'end':
#     s.append([int(i) for i in a.split()])
#     a = input()
# for i in range(len(s)):
#     for j in range(len(s[0])):
#         print(s[i-1][j] + s[i+1-len(s)][j] + s[i][j-1] + s[i][j+1 - len(s[0])], end=' ')
#     print()
#
# c = []
# while True:
#     a = [i for i in input().split()]
#     if a == ['end']:
#         break
#     c.append(a)
# n, m = len(c), len(c[0])
# for i in range(n):
#     for j in range(m):
#         x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
#         print(x, end=' ')
#     print()

# x = int(input())
# s = [[n+1 for n in range(x)] for m in range(x)]
# a = x
# step = 0
# while a != x * x:
#     for m in range(1 + step, x - step):
#         n = x - 1 - step
#         a += 1
#         s[m][n] = a
#     for n in range(x - 2 - step, -1 + step, -1):
#         m = x - 1 - step
#         a += 1
#         s[m][n] = a
#     for m in range(x - 2 - step, 0 + step, -1):
#         n = 0 + step
#         a += 1
#         s[m][n] = a
#     for n in range(1 + step, x - 1 - step):
#         m = 1 + step
#         a += 1
#         s[m][n] = a
#     step += 1
# for m in range(x):
#     for n in range(x):
#         print(s[m][n], end=' ')
#     print()
#
# n=int(input())
# t=[[0]*n for i in range (n)]
# i,j=0,0
# for k in range(1, n*n+1):
#   t[i][j]=k
#   if k==n*n: break
#   if i<=j+1 and i+j<n-1: j+=1
#   elif i<j and i+j>=n-1: i+=1
#   elif i>=j and i+j>n-1: j-=1
#   elif i>j+1 and i+j<=n-1: i-=1
# for i in range(n):
#   print(*t[i])
#
# n = int(input())
#
# # Создаем нулевую квадратную матрицу заданной размерности
# a = [[0 for i in range(n)] for j in range(n)]
#
# # Определяем внутренние счетчики для цикла
# i = 0  # строки
# j = 0  # столбцы
# x = 1  # текущее значение для заполнения ячейки
# k = 0  # порядковый номер контура
#
# while x <= n * n:
#     a[i][j] = x  # заполняем ячейку текущим значением
#
#     if i != j:  # Только если мы сейчас не на диагонали!
#         # Сумма зеркально расположенных элементов одинакова для текущего контура.
#         # Она равна нижнему правому значению в контуре, умноженному на 2.
#         # Так что на каждом шаге цикла мы заполняем зеркальный элемент матрицы,
#         # просто вычитая текущее x из этой суммы ;)
#         a[j][i] = (a[k][k] + (n - k * 2) * 2) * 2 - 4 - x
#
#     if j != n - k - 1:
#         # если еще не уперлись в правую границу контура, двигаемся вправо
#         j += 1
#
#     elif i != n - k - 1:
#         # если еще не уперлись в нижнюю границу контура, двигаемся вниз
#         i += 1
#
#     elif x != n * n:
#         # Если вправо и вниз уже нельзя, значит мы закончили обход текущего контура!
#         # Только не забываем проверить, что x не равен n*n, а то будет бо-бо.
#         k += 1  # переходим к следующему контуру
#         i = j = k  # обход следующего контура начнем с координат [k,k]
#         x = a[k][k - 1]  # текущее значение равно наибольшему в старом контуре
#
#     x += 1  # Ну, и не забываем прибавлять единичку в конце цикла, какое бы условие ни сработало.
#
# # Выводим на печать
# for i in a: print(*i)
#
# n = int(input())
# x,y,dx,dy, m = 0,0,0,1, [[0]*n for i in range(n)]
# for i in range(n*n):
#   m[x][y]=str(i+1)
#   if x+dx>=n or x+dx<0 or y+dy>=n or y+dy<0 or m[x+dx][y+dy]:
#       dx,dy = dy,-dx
#   x,y = x+dx, y+dy
# print("\n".join([" ".join(i) for i in m]))
# '''
# Один из немногих вариантов решения задачи, который мне кажется интуитивно понятным.
# Суть в том, что мы заполняем четыре (n-1) верхних символа двумерного массива начиная от самого начала
#  (a[0][0]), высотой и шириной равным пяти (n), оставляя последний символ, который после поворота становится нулевым.
# Затем поворачиваем массив против часовой стрелки 4 раза, заполняя каждую внешнюю сторону массива. После чего
#  происходит смещение "каретки" на внутренний периметр массива(a[1][1]).
#  '''
# x,i,j=1,0,0; n=int(input())
# a=[[0]*n for i in range (n)]
# a[n//2][n//2]=n**2
# for s in range (n//2):
#     for rotate in range (4):
#         for j in range (n-1-s*2):
#             a[i+s][j+s]=x
#             x=x+1
#         a=[[a[i][j] for i in range(n)] for j in range (n-1,-1,-1)]
# for i in a:
#     print(*i)
#
#
# n = int(input())
# m = [[0] * n for i in range(n)]
# i, j, di, dj = 0, 0, 0, 1
#
# for k in range(n * n):
#     m[i][j] = k + 1
#     if (not -1 < i + di < n) or (not -1 < j + dj < n) or m[i + di][j + dj] != 0:
#         di, dj = dj, -di
#     i, j = i + di, j + dj
#
# [print(*i) for i in m]
# b = -3

#
# def f(x):
#     res = 0
#     if x <= -2:
#         res = 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         res = - x / 2
#     else:
#         res = (x - 2) ** 2 + 1
#     return res
#
#
# print(f(-2))
#
#
# def f(x):
#     if x <= -2:
#         return 1 - (x+2)**2
#     if x <= 2:
#         return -x/2
#     return (x-2)**2 + 1
#
#
# def f(x):
#     return {
#         x <= -2:
#             1 - (x + 2) ** 2,
#         -2 < x <= 2:
#             -x / 2,
#         2 < x:
#             (x - 2) ** 2 + 1
#     }[True]

#
# lst = [1, 1, 3, 2, 4, 5, 6, 8, -1, 7, 8, 9, -16, 0, 4]
#
#
# def modify_list(l):
#     a = len(l) - 1
#     for i in reversed(l):
#         if i % 2 == 0:
#             l.append(int(i / 2))
#         del l[a]
#         a += - 1
#     return l.reverse()
#
#
# modify_list(lst)
# print(lst)
#
# """
# for x in l[:] - перебор элементов ведём по копии списка, полученной с помощью среза, т.к. исходный список мы меняем
# прямо во время прохода, а в этом случае простой поэлементный перебор "ломается".
# """
#
# def modify_list(l):
#     for x in l[:]:
#         if x % 2 == 0:
#             l.append(x//2)
#         l.remove(x)
#
# def modify_list(l):
#     i=0
#     while i<len(l):
#         if l[i]%2 !=0:
#             del (l[i])
#         else:
#             l[i]=l[i]//2
#             i+=1
#
# """
# Срез позволяет изменить элементы списка, остальное делается генератором.
# """
#
# def modify_list(l):
#     l[:] = [i//2 for i in l if i % 2 == 0]
#
#
# def modify_list(l):
#     for i in reversed(range(len(l))):
#         if l[i] % 2 == 1:
#             del l[i]
#         else:
#             l[i] //= 2
#
# """
# Используется интересный способ по изменению элементов массива через присваивание элементов из нового массива b
#  в исходный l.
# """
# def modify_list(l):
#     b = []
#     for x in l:
#         if x % 2 == 0:
#             b.append(x // 2)
#     l[:] = b

#
# d = {}
#
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     elif 2 * key in d:
#         d[2 * key].append(value)
#     else:
#         d[2 * key] = [value]
#
#
# update_dictionary(d, 1, -1)
# print(d)
# update_dictionary(d, 2, -2)
# print(d)
# update_dictionary(d, 1, -3)
# print(d)
#
# def update_dictionary(d, key, value):
#     key += key * (key not in d)
#     d[key] = d.get(key, []) + [value]
#
# def update_dictionary(d, key, value):
#     if key in d:  # if key in d.keys():
#         d[key] += [value]
#     elif 2 * key in d:
#         d[2 * key] += [value]
#     else:
#         d[2 * key] = [value]
#
#
# dictionary = {}
# words = input().lower().split()
# for key in words:
#     if key in dictionary:
#         dictionary[key] += 1
#     else:
#         dictionary[key] = 1
# for key, value in dictionary.items():
#     print(key, value)
#
# dictionary = {'a': 1, 'b': 2, 'c':3}
# print(dictionary)
# for key,value in dictionary.items():
#     print(key, ':', value)
# for key in dictionary.keys():
#     print(key)
# for value in dictionary.values():
#     print(value)
#
#
#
#
# # put your python code here
# s = input().lower().split()
# for i in set(s):
#     print(i, s.count(i))
#
# text = input().lower().split()
# dictionary = dict()
# for word in text:
#     if(word not in dictionary):
#         dictionary[word] = 1
#     else:
#         dictionary[word]+=1
# for word, count in dictionary.items():
#     print(word, count)
#
# x = input().lower().split()
# a = {i:x.count(i)for i in x}
# for i,j in a.items():
#   print(i,j)

#
# def f(x):
#     return x + 100
#
# dictionary = {}
# repeat = int(input())
# result = []
# for member in range(repeat):
#     number = int(input())
#     if number not in dictionary:
#         dictionary[number] = f(number)
#     result.append(dictionary[number])
# print(*result, sep='\n')
#
# cache = {}
# for _ in range(int(input())):
#     x = int(input())
#     if x not in cache:
#         cache[x] = f(x)
#     print(cache[x])
#
# # На удивление цикл  'while' сработал более продуктивно, чем 'for i in range(n)'
# # Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
# n,d,i = int(input()), {},0
# while i < n:
#     key, i  = int(input()), i+1
#     if key not in d:
#         d[key] = f(key)
#     print(d[key])
#
# with open('D:\\dataset_3363_2.txt', 'r') as original_file:
#     str_in = original_file.readline().strip() + "*"
# # str_in = input() + "*"
# str_out, a, b = '', '', '0'
# for i in str_in:
#     if i.isdigit():
#         b += i
#         continue
#     str_out += a * int(b)
#     a = i
#     b = ''
# # print(str_out)
# with open('D:\\dataset.txt', 'w') as decoded_file:
#     decoded_file.write(str_out)
#     # decoded_file.write(str(1))
#
# """
# Первый символ - гарантированно буква.
# Перебираем все последующие, пока они цифровые или пока не достигнут конец строки.
# После внутреннего цикла j либо указывает на следующую букву, либо на конец строки.
# В обоих случаях между s[i] и s[j] - цифры, составляющие нужное нам число повторов символа s[i].
# Печатаем символ нужное число раз, присваиваем i индекс следующей буквы для новой итерации цикла
# """
# with open('dataset_3363_2.txt', 'r') as f:
#     s = f.readline().strip()
# i = 0
# while i < len(s):
#     j = i + 1
#     while j < len(s) and s[j].isdigit():
#         j += 1
#     print(s[i] * int(s[i+1:j]), end='')
#     i = j
#
#
# s, d = input(), []
# for i in s:
#     if not i.isdigit(): d.append(i)
#     else: d[-1] += i
# print(*[i[0]*int(i[1:]) for i in d], sep='')

#
# text = open('D:\\dataset_3363_3.txt', 'r')
# s = text.read().replace('\n', ' ').lower().split()
# text.close()
# # s = input().lower().split()
# s.sort()
# a = 0
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         continue
#     if s.count(s[a]) < s.count(s[i + 1]):
#         a = i + 1
# print(s[a], s.count(s[a]))
#
# with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
#     maxc = 0
#     s = inf.read().lower().strip().split()
#     s.sort()
#     for word in s:
#         counter = s.count(word)
#         if counter > maxc:
#             maxc = counter
#             result_word = word
#     ouf.write(result_word +' ' + str(maxc))
# # Без словаря, сразу читаем файл и сортируем список слов, чтобы потом первое найденное было лексиграфически впереди.
#
# with open('words.txt') as f:
#     text = f.read().lower().split()
# popular_word = max(set(text), key=text.count)
# print(popular_word, text.count(popular_word))
# """
# это именованный параметр функции,который отвечает за критерий сравнения для поиска максимального значения.
# В данном случае у нас есть множество уникальных слов ,которые содержатся в  файле(это наша коллекция(set(text) к
# которой применяется функция max ) и мы хотим вернуть самое популярное ,которое чаще всего будет встречаться в тексте.
# Благодаря ключевому слово key =  мы можем передать любую функцию/метод ,в данном случае передаем count отвечающий за
# подсчет количества вхождений данного слова в тексте,которая/ый будет применяться к каждому элементу коллекции.
# Вот вам пример, где сначала мы ведем поиск с критерием по умолчанию (лексикографически ) , а затем  находим максимум
# по ключевому слову int.
# lis = ['1','100','111','2']
# print(max(lis))#2
# print(max(lis,key = lambda x: int(x)))#111
# print(max(lis,key = int))#111
# """
"""
# Для тех, кто хочет сократить свой код :) написал небольшое руководство по [list comprehension]
# на основе примера на stackoverflow.com
# # http://stackoverflow.com/questions/16632124/python-emulate-sum-using-list-comprehension
# я немного изменил этот пример, чтобы лучше объяснить работу [list comprehension]
# и вам было проще понять, как применить этот подход к решению задания

# допустим, у нас есть список фруктов, где зафиксированы самые низкие и высокие цены на эти фрукты
# т.е. по сути это список списков :)
lst = [["apple", 55, 62], ["orange", 60, 74], ["pineapple", 140, 180], ["lemon", 80, 84]]

# выведем этот список для нагляности на экран, используя [list comprehension]
[print(el) for el in lst]
# ['apple', 55, 62]
# ['orange', 60, 74]
# ['pineapple', 140, 180]
# ['lemon', 80, 84]

# если мы хотим подсчитать среднюю цену на каждый из фруктов, то напишем что-то вроде
sumMiddle = 0
for el in lst:
    sumMiddle = (el[1] + el[2]) / 2
    print(sumMiddle)

# или можно сделать это одной строкой
[print((priceLow + priceHigh) / 2) for fruit, priceLow, priceHigh in lst]
# представьте, что наш список списков - это таблица из трёх столбцов
# и мы можем обращаться к столбцам, просто озаглавив их fruit, priceLow, priceHigh
# в цикле for, почти как перебор элементов словаря for key, value in d.items() :)

# поэтому, когда вы захотите прикинуть, сколько же, от и до, в среднем может стоить
# ваша фруктовая корзина, нужно будет посчитать среднее по каждой колонке
# вы можете сделать это примерно так
sumLow, sumHigh = 0, 0
for el in lst:
    sumLow += el[1]
    sumHigh += el[2]
sumLow /= len(lst)
sumHigh /= len(lst)
print(sumLow, sumHigh)

# или применить кунг-фу списковых выражений и обойтись парой строк :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst))
print(sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# а где два принта, там и один :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst), sum([priceHigh for fruit, priceLow, >>>
>>>priceHigh in lst]) / len(lst))

# надеюсь, вам было понятно и интересно
# желаю успехов в учёбе!!!
"""

# У кого проблема с русскими фамилиями в винде помогает
# with open("file.txt", "r", encoding='utf-8') as file:

"""
Если в функции print использовать file = имя переменной, то принтоваться будет непременно в файл, тем самым можно
добавлять в файл большое кол-во элементов без использования форматирования строк.
Пример:
in_ = open('file.txt', 'r')
out_ = open('output.txt' , 'w')
print(1, 2, 3, 4, file = out_) #ничего не выводится
вместо
in_ = open('file.txt', 'r')
out_ = open('output.txt' , 'w')]
a = 1
b = 2
c = 3
d = 4
out_.write(' {}, {}, {}, {}'.format(a, b, c, d))
"""
"""
Часто возникали сложности с методом write. Нашел еще одну конструкцию для записи в файл c помощью всем известного print:
with open('filename.txt', 'w') as inf:
.....
    print(some text or numbers, file = inf)
Может кому поможет
"""

#
# with open('D:\\dataset_3363_4.txt', 'r') as inf, open('D:\\dataset_out.txt', 'w') as ouf:
#     s = inf.read().strip().split('\n')
#     out, out1 = [], []
#     a, b, c = 0, 0, 0
#     for i in s:
#         d = (i.split(';'))
#         out.append(round((int(d[1]) + int(d[2]) + int(d[3])) / 3, 9))
#         a += int(d[1])
#         b += int(d[2])
#         c += int(d[3])
#     print(*out, sep='\n', file=ouf)
#     for i in (a, b, c):
#         e = round(i / len(s), 9)
#         out1.append(e)
#     print(*out1, sep=' ', file=ouf)
#
# koll, a1, b1, c1 = 0, 0, 0, 0
# with open('dataset_3363_4.txt', 'r') as inf:
#     for line in inf:
#         line = line.strip().split(';')
#         a, b, c = int(line[1]), int(line[2]), int(line[3])
#         print((a+b+c)/3)
#         koll += 1
#         a1 += a
#         b1 += b
#         c1 += c
# print((a1/koll), (b1/koll), (c1/koll))
#
# sum, psum, rsum, n = 0, 0, 0, 0
# stroka = ''
# with open('in.txt') as inf, open("out.txt", 'w') as file_out:
#     for line in inf:
#         line = line.strip().split(';')
#         stroka = stroka  + str(((int(line[1])+int(line[2])+int(line[3]))/3))+ '\n'
#         msum += int(line[1])
#         psum += int(line[2])
#         rsum += int(line[3])
#         n += 1
#     stroka = stroka +  str(msum/n) + ' ' +str(psum/n) + ' '+ str(rsum/n)
#     file_out.write(stroka)
#
#
# st = [x.split(';') for x in open('fl.txt').readlines()]
# print(*[sum([int(y) for y in x[1:]])/3 for x in st], sep='\n')
# print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]])/len(st) for z in range(1,4)])
#
# Звезда используется для запаковки и распаковки последовательностей - https://www.python.org/dev/peps/pep-3132/
# >>> a, *b, c = range(5)
# >>> a, c
# (0, 4)
# >>> b[1, 2, 3]
# >>> print(*b)
# 1 2 3
#
# f = [i.strip().split(';') for i in open('file.txt', encoding='utf-8').readlines()]
# print(*[sum([int(y) for y in x[1:]]) / 3 for x in f], sep='\n')
# print(*[sum([int(y[x]) for y in f]) / len(f) for x in range(1, 4)])
#
#
# import pandas as pd
#
# df = pd.read_csv('dataset_3363_4.txt', sep=';', names=['Фамилия','Математика', 'Физика', 'Русский язык'])
# mat = df['Математика'].mean()
#
# phis = df['Физика'].mean()
#
# rus = df['Русский язык'].mean()
#
# df['Среднее ученика'] = (df['Математика'] + df['Физика'] + df['Русский язык']) / 3
#
# mean_learn = df['Среднее ученика']
#
# with open('result.txt', 'w') as file:
#     for value in mean_learn:
#         file.write(str(value)+'\n')
#     file.write(str(mat)+' '+str(phis)+' '+str(rus))

# import math
# r = float(input())
# print(2 * math.pi * r)
#
# from math import pi
# print(float(input()) * pi * 2)
#
# from math import tau
# print(float(input()) * tau)  # tau = 2pi

#
# import sys
# s = sys.argv
# print(*s[1:], end=' ')
#
# import sys
# print(*sys.argv[1:])

# import requests
#
# with open('D:\\dataset_3378_2.txt', 'r') as inf:
#     s = inf.read().strip()
# r = requests.get(s)
# # print(r.text)
# print(len(r.text.splitlines()))
#
#
# with open('dataset_3378_2.txt') as inf:
#     r = requests.get(inf.readline().strip())
#     print(len(r.text.splitlines()))
#
# from requests import get
# with open('dataset.txt') as f:
#     url = f.readline().strip()
# text = get(url).text.splitlines()
# print(len(text))
#
#
# import requests
# print(len(requests.get(open('dataset.txt').readline().strip()).text.splitlines()))
#
# import requests
#
# with open('D:\\dataset_3378_3.txt') as inf:
#     p = inf.read().strip()
# s = requests.get(p)
# while True:
#     if not s.text.startswith('We'):
#         print(s.text)
#         s = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + s.text)
#         continue
#     else:
#         print(s.text)
#         break
#
# import requests
# url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt'
# while name[:2] != 'We':
#     name = requests.get(url + name).text
# print(name)
#
# import requests
#
# def req(filename):
#     r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + filename)
#     if r.text.split()[0] != 'We':
#         return req(r.text)
#     else:
#         return r.text
#
# print(req('699991.txt'))
#
#
# import requests
# with open ('dataset_3378_3.txt','r') as f:
#     txt=f.read()
# counter=0
# while True:
#     if txt[:2]=='We':
#         print(txt)
#         break
#     else:
#         counter+=1
#         print('переход по ссылке №', counter)
#         if counter==1:
#             url=txt.strip()
#         else:
#             url='https://stepic.org/media/attachments/course67/3.6.3/'+txt.strip()
#         print(url)
#         r=requests.get(url)
#         txt=r.text
#
# number_games = int(input())
# dist, res = [], []
# for i in range(number_games):
#     dist.append(input().split(';'))
#     for j in [0, 2]:
#         if dist[i][j] not in res:
#             res.append(dist[i][j])
#             for s in range(5):
#                 res.append(0)
#     a, b = 0, 2
#     if int(dist[i][1]) == int(dist[i][3]):
#         for j in [0, 2]:
#             res[res.index(dist[i][j]) + 1] += 1
#             res[res.index(dist[i][j]) + 3] += 1
#             res[res.index(dist[i][j]) + 5] += 1
#     else:
#         if int(dist[i][1]) < int(dist[i][3]):
#             a, b = 2, 0
#         res[res.index(dist[i][a]) + 1] += 1
#         res[res.index(dist[i][a]) + 2] += 1
#         res[res.index(dist[i][a]) + 5] += 3
#         res[res.index(dist[i][b]) + 1] += 1
#         res[res.index(dist[i][b]) + 4] += 1
# for i in range(int(len(res) / 6)):
#     print(str(res[i * 6]) + ':', end='')
#     print(*res[1 + i * 6: 6 + i * 6])
#
# """
# если кто-то собирает данные в словарь в формате key=команда, values=список состоящий из игр, побед, ничьих,
# поражений и очков. то для корректного вывода как просят в задаче рекомендую следующий синтаксис:
# for q, w in d.items():
#     print((q+':'), *w, end='\n')
# Вполне возможно, что кому-то поможет комментарий из раздела "Словари", т.к. в лекции этой информации не было:
# "Иллюстрация, как обращаться к элементу списка, если такой список является значением в словаре:
# example = {'A': [22, 33, 44], 'B': [10, 20]}
# print(example['A'][1])
# """
#
# def command(c, res):
#     if not c in dct: dct[c] = [0, 0, 0, 0, 0]
#     dct[c] = [dct[c][0] + 1,
#                 dct[c][1] + 1 if res == 3 else dct[c][1],
#                 dct[c][2] + 1 if res == 1 else dct[c][2],
#                 dct[c][3] + 1 if res == 0 else dct[c][3],
#                 dct[c][4] + res,]
# dct = {}
# for i in range(int(input())):
#     c1, g1, c2, g2 = input().split(';')   #  g1, g2 = int(g1), int(g2)
#     command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
#     command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
# for c in dct:
#     print('{}:{} {} {} {} {}'.format(c, *dct[c]))
#
# n = int(input())
# teams = {}
# for i in range(n):
#     team1, goal1, team2, goal2 = input().split(';')
#
#     if team1 not in teams:
#         teams[team1] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}
#
#     if team2 not in teams:
#         teams[team2] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}
#
#     if goal1 > goal2:  # team1 wins
#         teams[team1]['wins'] += 1
#         teams[team1]['score'] += 3
#
#         teams[team2]['loses'] += 1
#         teams[team2]['score'] += 0
#
#     elif goal2 > goal1:  # team2 wins
#         teams[team1]['loses'] += 1
#         teams[team1]['score'] += 0
#
#         teams[team2]['wins'] += 1
#         teams[team2]['score'] += 3
#
#     elif goal1 == goal2:  # draw
#         teams[team1]['draws'] += 1
#         teams[team1]['score'] += 1
#
#         teams[team2]['draws'] += 1
#         teams[team2]['score'] += 1
#
#     teams[team1]['plays'] += 1
#     teams[team2]['plays'] += 1
#
# for team in teams:
#     values_order = ['plays', 'wins', 'draws', 'loses', 'score']
#     print("{}:{}".format(str(team), ' '.join([str(teams[team][key]) for key in values_order])))
#
#
# def points_counter(team, goals1, goals2):
#     if team not in d:
#         d[team] = [0] * 5
#     d[team][0] += 1
#     d[team][1] += int(goals1 > goals2)
#     d[team][2] += int(goals1 == goals2)
#     d[team][3] += int(goals1 < goals2)
#     d[team][4] += int(goals1 > goals2) * 3 + int(goals1 == goals2)
#
# n, d = int(input()), {}
# for _ in range(n):
#     k = input().split(';')
#     points_counter(k[0], int(k[1]), int(k[3]))
#     points_counter(k[2], int(k[3]), int(k[1]))
# for k, v in d.items():
#     print(k + ":" + str(v[0]), v[1], v[2], v[3], v[4])
#
#
# a=[input().split(';') for i in range(int(input()))]
# b={i:[] for i in set([i[0] for i in a])|set([i[2] for i in a])}
# for i in a:
# 	b[i[0]].append(1 if i[1]==i[3] else 3 if i[1]>i[3] else 0)
# 	b[i[2]].append(1 if i[1]==i[3] else 3 if i[1]<i[3] else 0)
# for i in b: print('%s:%i %i %i %i %i'%(i,len(b[i]),b[i].count(3),b[i].count(1),b[i].count(0),sum(b[i])))
# """
# Генератор словаря.
# В классическом виде можно переписать так:
# b={}
# for i in set([i[0] for i in a])|set([i[2] for i in a]):
#  b[i]=[]
# set - множество - список неповторяющихся элементов.
# | - объединение двух множеств. Множество неповторяющихся элементов первого и второго списка.
# Т.е. формируем список команд из первого столбца [i[0] for i in a]. Тут могут быть повторения. Избавляемся от
# повторений преобразуя список в множество set([i[0] for i in a]). Тоже самое делаем для 3 столбца. Далее составляем
# множество из # всех возможных названий команд первого и третьего столбца:
# set([i[0] for i in a])|set([i[2] for i in a]). Далее
# формируем словарь, где каждому названию команды ставим в соответствие пустой список:
# b={i:[] for i in set([i[0] for i in a])|set([i[2] for i in a])}
# Далее каждой команде добалвяем в список 3 балла за победу, 1 за ничью строки и 0 за поражение строки 2-5.
# Потом для каждой команды считаем количество элементов в списке (количество игр), количество троек (выигрыши),
# количество 1 (ничьи), количество (0) - проигрыши и сумму элементов списка (сумму очков) и выводим на экран  - 6 строка
# """

# не помню я в этом курсе очень удобную функцию для создания словаря - zip
# Работает так:
# a = dict(zip(b,c))
# В итоге создается словарь a  в котором ключи - это данные из списка b, а значения  - данные из c
# (для нашей программы b и c могут быть строками из ввода!)
# Для корректной работы необходимо, чтобы b и c были одной длины
#
# инверсия словаря!
# dict = {v:k for k, v in dict.items()}
#
# Может кому будет полезно:
# e = {}
# ...
# for i, v in e.items(): # можно перебирать и ключи (i) и значения (v) всего списка (e.items())
#     if v == element: # а работать, например, только со значениями

#
# def out_code(x, y):
#     for i in range(len(x)):
#         for key in y:
#             if x[i] == key:
#                 x += y[key]
#     x = x[int(len(x) / 2):]
#     print(x)
#
#
# b, c = str(input()), str(input())
# a = dict(zip(b, c))
# d = dict(zip(c, b))
# b, c = str(input()), str(input())
# out_code(b, a)
# out_code(c, d)
#
# a,b,c,d=input(),input(),input(),input()
# print(''.join(b[a.index(i)] for i in c))
# print(''.join(a[b.index(i)] for i in d))
#
# # Считываем 4 строки в цикле
# original, coding, first_string, second_string = (input() for i in range(4))
#
# # По индексу символа из оригинала берём символ на замену из кодировки,
# # для каждого символа из строки, которую нужно закодировать
# print(*[coding[original.find(symbol)] for symbol in first_string], sep='')
# # Аналогично, только наоборот :D
# print(*[original[coding.find(symbol)] for symbol in second_string], sep='')
#
# def code(source, end, data):
#     ''' Data coder '''
#     cryptData = ''
#     for char in data:
#         cryptData += end[source.index(char)]
#     return cryptData
#
# # Input data
# key1 = input()
# key2 = input()
# decode = input()
# encode = input()
#
# print(code(key1, key2, decode))
# print(code(key2, key1, encode))
#
# x=input()
# y=input()
# X=input()
# Y=input()
# d={}
# for i in range(0,len(x)):
#     d[x[i]]=y[i]
# for i in range(0,len(X)):
#     print(d[X[i]],end='')
# print('')
# for i in range(0,len(Y)):
#     for key in d.keys():
#         if Y[i]==d[key]:
#             print(key,end='')

#
# words, text, prt = [], [], []
# for i in (words, text):
#     number = int(input())
#     for j in range(number):
#         i += input().lower().split()
# for i in range(len(text)):
#     if text[i] not in words and text[i] not in prt:
#         prt.append(text[i])
#         print(text[i])
#
#
# # формируем множество известных слов на основании построчного ввода
# dic = {input().lower() for _ in range(int(input()))}
# # заводим пустое множество для приема текста
# wrd = set()
# # т.к. текст построчно подается, а также в каждой строке несколько слов,
# # то каждую строку превращаем во множество и добавляем в единое множество wrd
# for _ in range(int(input())):
#     wrd |= {i.lower() for i in input().split()}
# # на вывод отправляем результат вычитания словарного множества dic
# # из текстового множества wrd; впереди ставим *, чтобы раскрыть поэлементно
# print(*(wrd-dic), sep="\n")
#
# count_dict = int(input())
# dict = []
# check_words = []
# result = []
# #заполняем словарь
# for i in range(count_dict):
#   dict.append(input().lower())
# count_lines = int(input())
# #заполняем список проверяемых слов
# for i in range(count_lines):
#   check_words += input().lower().strip().split(' ')
# #выбираем слова которые не проходят проверку
# for i in check_words:
#   if i not in dict and i not in result:
#     result.append(i)
# #печатаем
# for i in result:
#   print(i)
#
# мой вариант решения: 1) заполняем словарь; 2) преобразуем текст в множество слов; 3) печатаем разность двух множеств
# # put your python code here
# words = set(input().lower() for i in range(int(input())))
# text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
# print('\n'.join(text - words))

#
# a, b = 0, 0
# data = [input().split() for _ in range(int(input()))]
# for i in range(len(data)):
#     if data[i][0] == 'восток':
#         a += int(data[i][1])
#     elif data[i][0] == 'запад':
#         a -= int(data[i][1])
#     elif data[i][0] == 'север':
#         b += int(data[i][1])
#     elif data[i][0] == 'юг':
#         b -= int(data[i][1])
# print(a, b)
#
#
# n=int(input())
# d={'север':0,'запад':0,'юг':0,'восток':0}
# for i in range(n):
#     x=input().split()
#     d[x[0]]+=int(x[1])
# print(d['восток']-d['запад'], d['север']-d['юг'])
#
#
# dict = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}
# for _ in range(int(input())):
#     key, value = input().split()
#     dict[key] += int(value)
# print(dict['восток'] - dict['запад'], dict['север'] - dict['юг'])
#
# k=[0,0]
# for i in range(int(input())):
#     a=[str(i) for i in input().split()]
#     if a[0]=='север':
#         k[1]+=int(a[1])
#     if a[0]=='восток':
#         k[0]+=int(a[1])
#     if a[0]=='юг':
#         k[1]-=int(a[1])
#     if a[0]=='запад':
#         k[0]-=int(a[1])
# print(k[0],k[1],sep=' ')
#
# cor = {'север': 0, 'восток': 0, 'юг': 0, 'запад': 0}
# for i in range(int(input())):
#     s = [j for j in input().split()]
#     cor[s[0]] += int(s[1])
# print(cor['восток']-cor['запад'], cor['север']-cor['юг'])
#
# x,y=0,0
# for i in range(int(input())):
#     s=input().split()
#     x+=int(s[1])*((s[0]=='восток')-(s[0]=='запад'))
#     y+=int(s[1])*((s[0]=='север')-(s[0]=='юг'))
# print(x,y)
#
# def main():
#     a, b = map(int, input().split())
#     res = a + b
#     print(res)
#
# if __name__ == "__main__":
#     main()


