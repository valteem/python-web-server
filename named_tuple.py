from collections import namedtuple

CustomColl = namedtuple('CustomCollection', ['Method','URL', 'ver'])
cu = CustomColl('GET', '/users?name=Name', 'HTTP/1,1')
print(cu)
print(cu.URL)