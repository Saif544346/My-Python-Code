'''n=int(input("enter n:"))
for x in range(n+1):
    print((2*x-1)*"*")
    enter
    n: 5

    *
    ** *
    ** ** *
    ** ** ** *
    ** ** ** ** *
    '''
'''n=int(input("Enter n:"))
for x in range(n+1):
    print(x*"*")
    Enter
    n: 3

    *
    **
    ** *
    '''
rows = 6
for row in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
