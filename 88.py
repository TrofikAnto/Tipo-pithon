def Median(a, b, c):
    import math
    med=math.sqrt((2*a**2+2*b**2-c**2)/(4))
    print("Медиана равна : ", med)
print("\tВычисление медианы по трем сторонам треугольника") 
a=input("Введите первое значение: ") 
b=input("Введите второе значение: ") 
c=input("Введите третье значение: ") 
if (a.isdigit()==True and b.isdigit()==True and c.isdigit()==True):
    a=int(a); b=int(b); c=int(c)   
    if (a<=0 or b<=0 or c<=0):
        print("Введенные значения меньше нуля")
    else:
        Median(a, b, c)
else:
    print("Неверные значение")