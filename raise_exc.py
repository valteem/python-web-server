import sys

keyword = sys.argv[1]
while True:
    if keyword == 'quit':
        print('quitting')
        raise Exception('Keyword ''quit'' detected')
print('end of logic')