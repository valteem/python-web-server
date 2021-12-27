import sys

filename = sys.argv[1]

f = open(filename, 'rb')
raw = f.readline(64)
print("Binary format:",raw)
req = str(raw,'iso-8859-1')
print("String format:", req)