from functools import lru_cache

class Example:
    def __init__(self, inp):
        self._inp = inp
    @lru_cache
    def wrap(self):
        return '<' + self._inp + '>'

e3 = Example('txt')
e3.wrap()
e3.wrap()
e3.wrap()

e4 = Example('num')
e4.wrap()
e4.wrap()
e4.wrap()

print(Example.wrap.cache_info())

e5 = Example('txt')
e5.wrap()
e5.wrap()

print(Example.wrap.cache_info())

e11 = Example('t1')
e11.wrap()
e12 = Example('t1')
e12.wrap()
e13 = Example('t1')
e13.wrap()
e14 = Example('t1')
e14.wrap()

print(Example.wrap.cache_info())