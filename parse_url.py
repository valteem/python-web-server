from urllib.parse import parse_qs, urlparse

class Request:
    def __init__(self, method, target, ver):
        self.method = method
        self.target = target
        self.ver = ver
    @property
    def url(self):
        return urlparse(self.target)
    @property
    def path(self):
        return self.url.path
    @property
    def query(self):
        return parse_qs(self.url.query)

req = Request('GET', '/users?name=vasya&age=30','HTTP/1.1')
print(req.__dict__)
print(urlparse('/users?name=vasya&age=30'))
print(req.path)
print(req.query)