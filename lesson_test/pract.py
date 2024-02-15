# def append_list(val, my_list=[]):
#     my_list.append(val)
#     return my_list
#
#
# list1 = append_list(10)
# list2 = append_list(123, [])
# list3 = append_list('a')
# print(list1)  # [10, 'a']
# print(list2)  # [123]
# print(list3)  # [10, 'a']
#
# x = [1, 2, 3]
# y = x


print(3 or 4)

print(int('100', 0))
print(int('1000', 16))

x = int('1' * 1111)
print(x)
print(len(str(x)))

print((1, 2) + (1, 2))


# print(1 in '123')


x = 0
def bar():
    return x + 1


print(bar())

a = False
b = 0

print(not b is a)

for i in range(1):
    print(1)
else:
    print(2)
