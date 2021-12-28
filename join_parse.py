from email.parser import Parser

a = ['Host: example.local','Accept: text/html', 'UserAgent: Mozilla/5.0']
b = ''.join(a)
print(b)
c = Parser().parsestr(b)
for x in c:
    print(x,c[x],'\n')