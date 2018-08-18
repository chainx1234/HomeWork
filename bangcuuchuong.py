print(" \t \t \t \t Multiplication Table")
print("\t ", end='')
for i in range(1,10):

    print('%4d' %i,end='')
print('\n')
print('-'*50)
for i in range(1,10):
    count = i
    print(i,'| ', end='')
    for j in range(1,10):

        print('\t%d' %(i*j), end=' ')
    print('\n')
