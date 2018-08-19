# tinh tien trong tai khoan sau N thang
# co M dong, lai xuat la R, sau N thang
# goi so tien thang i la Ti, T1 = m*r +m = T0(1+r), thang 2 la: T2 = T1(1+r)= T0(1+r)(1+r)=T0(1+r)^2
m = float(input("nhap vao so tien gui: "))
n = float(input("nhap vao so thang gui: "))
r = float(input("nhap vao lai xuat: "))

def tinh_lai(m:float,r:float,n:float):
    Ts = m*pow(r+1,n)
    Tl = Ts - m
    return {"tongsotien":Ts,"sotienlai":Tl}

a = tinh_lai(m,r,n)
print(a)