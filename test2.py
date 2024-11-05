count = [100,200,300,400,500,600,700,800,900,1000]


for i, in count:
    print(i)
for i in count:
    print(i)

    import sys

    for line in sys.stdin:
        if 'q' == line.rstrip():
            break
        print(f'Input : {line}')

    print("Exit")