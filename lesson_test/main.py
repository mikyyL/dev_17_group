# def avg(ranks):
#     assert len(ranks) != 0, 'expected len list not zero'
#     return sum(ranks) / len(ranks)
#
#
# my_list = []
# new_list = [1, 2, 3]
# print(f'среднее значение: {avg(new_list)}')

# def func1(n):
#     assert type(n) == int, f'expected not empty list'
#     lst = [2 ** i for i in range(n)]
#     return lst
#
#
# print(func1(4))
#
# my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# new_dict = {key + str(len(key)): my_dict[key] for key in my_dict}
# for key in new_dict:
#     assert key[-1].isdigit()
# print(new_dict)
# new_n_dict = {}
# for key in my_dict:
#     len_key = len(key)
#     new_n_dict[key + str(len_key)] = my_dict[key]
# print(new_n_dict)
#
# input_string = input('Введите строку: ')
# if len(input_string) > 10:
#     new_string = f'{input_string}!!!'
#     # print(new_string[-1:-4:-1])
#     assert new_string[-1:-4:-1] == '!!!'
#     print(new_string)
# else:
#     print(input_string[1])
#
# number = int(input('Введите число: '))
# new_dict = {n: {
#     'name': input('Введите значение name'),
#     'email': input('Введите значение email')
# }
#     for n in range(0, number)}
# assert len(new_dict.keys()) != 0
# print(new_dict)


a = int(input('введите число: '))
b = int(input('введите число: '))
new_list = []
for i in range(a, b+1):
    if i % 3 == 0:
        new_list.append(i)
print(new_list)
assert len(new_list) != 0
average = sum(new_list) / len(new_list)
assert average != 0
print(average)