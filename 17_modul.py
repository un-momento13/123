# создадим вечный цикл (пока True, или пока 1), в котором принудим пользователя вводить данные до тех пор,
# пока они не будут введены правильно:
while True:
    try:
        my_string = input('Введите 5 чисел через пробел: ').rstrip()
        array_str = my_string.split(' ')
        array_int = [int(i) for i in array_str]
        # попытаемся сразу преобразовать введенные символы в числовой тип, если при этом будет ошибка,
        # значит пользователь ошибся в вводе (ввел не только числа) - обработаем это исключение,
        # предложив пользователю ввести числа еще раз

        if len(array_int) != 5:
            print("Введите, пожалуйста, ровно 5 чисел")
            continue
        # также, если введено не 5 чисел, попросим пользователя еще раз ввести 5.
        # Если не добавить continue, цикл выйдет на break и заново введенные числа не будут проверяться.
        break
    except:
        print("Необходимо вводить только числа")

num = int(input('Введите любое число: '))


# функция сортировки по возрастанию, возьмем быструю сортировку:
def q_sort(array, left,
           right):  # left, right - это индексы крайних элементов из левой и правой части, от них будем отталкиваться
    middle = (left + right) // 2

    p = array[middle]  # присвоим переменной p значение индекса среднего элемента массива
    i, j = left, right  # элементы i - это будут элементы из левой части, а элементы j - из правой
    while i <= j:
        while array[i] < p:  # 1-й цикл: сравниваем поочередно элементы из левой части со средним
            i += 1
        while array[j] > p:  # 2-й цикл: сравниваем поочередно элементы из правой части со средним
            j -= 1
        if i <= j:  # 3-й цикл: меняем элементы из левой и правой частей местами
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        q_sort(array, left, j)  # рекурсивно вызываем эту же функцию, но берез новый диапазон
    if right > i:
        q_sort(array, i, right)


q_sort(array_int, 0, len(array_int) - 1)
print(f'Отсортированный массив: {array_int}')


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


# print(binary_search(array_int, num, 0, len(array_int) - 1))


def search(array_int, num):
    array_i = array_int
    # создадим новый массив, чтобы добавить туда введенное пользователем число
    array_i.append(num)

    q_sort(array_i, 0, len(array_i) - 1)
    x = len(array_i) - 1

    while True:
        index = binary_search(array_i, num, 0, x)
        if index == 0 or index == (len(array_i) - 1):
            return -1
        if array_i[index - 1] < num:
            return index - 1
        x = index


j = search(array_int, num)

if j < 0:
    print('Такого элемента нет')
else:
    print(f'Индекс элемента, удовлетворяющего условиям: {j}')