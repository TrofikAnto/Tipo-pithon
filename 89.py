def NumList(Value):
    List = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", ""]
    for i in range(len(List)):
        if (Value == i):
            i-=1
            print("Числительное:",List[i])
print("\tПеревод целых чисел в числительные")
Value = int(input("Введите целое число: "))
for i in range(1,13):
    if (Value == i):
        NumList(Value)