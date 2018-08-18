print("TIM USCLN")
a = int(input("nhap vao so tu nhien a: "))
b = int(input("nhap vao so tu nhien b: "))
Usc = 1
k = 2
while  k <= a and k <= b:
    if a%k == 0 and b%k ==0:
        Usc = k
    k += 1
print("USCLN la: ",Usc)


