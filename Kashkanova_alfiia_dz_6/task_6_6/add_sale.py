import sys

if len(sys.argv) < 2:
    sys.exit(0)



with open('bakery.csv','a', encoding='utf-8') as f:
    f.write('{}\n'.format(sys.argv[1]))
