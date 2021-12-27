import  sys

buffer = sys.argv[1]
pattern = sys.argv[2]

if pattern in buffer:
    print("Found!")
else:
    print("Not found")