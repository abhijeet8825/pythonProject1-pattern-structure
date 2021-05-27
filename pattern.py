x=input('Enter True or False\n')

def pattern(n):
    if x=='t':
        for i in range(n):
            for j in range(i+1):
                print('*',end='')

            print()

    else:
        for i in range(n):
            for j in range(n-i):
                print('*',end='')

            print()
pattern(6)



