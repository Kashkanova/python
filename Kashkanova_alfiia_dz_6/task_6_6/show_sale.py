import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    #lines = f.readlines()
    lines = []
    if len(sys.argv) == 1:
            lines = f.readlines()[:]
    if len(sys.argv) == 2:
            lines = f.readlines()[int(sys.argv[1])-1 : ]
    if len(sys.argv) == 3:
            lines = f.readlines()[int(sys.argv[1])-1 : int(sys.argv[2])]
    for line in lines:
        print(line.rstrip())