import time 
 
def hypotenuse(a, b): 
    return (a**2 + b**2)**0.5 
 
a = float(input("Введите длину первого катета: ")) 
b = float(input("Введите длину второго катета: ")) 
 
c = hypotenuse(a, b) 
print(f"Длина гипотенузы: {c:.2f}")
