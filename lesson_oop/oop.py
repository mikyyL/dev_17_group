# new -> объект класса -> init
class Point:
    def __new__(cls, *args, **kwargs):
        print(f'вызов __new__ для {cls}')
        return super().__new__(cls)

    def __init__(self, x, y):
        print(f'вызов __init__ для {self}')
        self.x = x
        self.y = y


point = Point(1, 2)
print(point)


class Counter:

    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__counter += 1
        return self.__counter


c = Counter()
c2 = Counter()
c()
c()
c()
result = c()
c2()
c2()
result2 = c2()
print(result)
print(result2)
