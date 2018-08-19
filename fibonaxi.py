# in ra day fibonaxi, tra lai so fibonaxi thu n

n = int(input("nhap vao so luong phan tu "))

def traso_fibonaxi(n:int):
    t1 = 0
    t2 = 1
    nexterm = 0
    for i in range(1,n+1):
        if i == 1:
            print(t1,end='     ')
            continue
        if i == 2:
            print(t2, end='     ')
            continue
        nexterm = t1 + t2
        t1 = t2
        t2 = nexterm
        print(nexterm, end='    ')
    return nexterm
fibo = traso_fibonaxi(n)
print('')
print('so fibonaxi thu %d la: %s'%(n,fibo))