import sys

def read_first_line(rfile):
    line = rfile.readline(32)
    print(line)

def read_second_line(rfile):
    line = rfile.readline(32)
    print(line)

filename = sys.argv[1]
rfile = open(filename, 'rb')
read_first_line(rfile)
read_second_line(rfile)