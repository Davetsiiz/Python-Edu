sayi1=int(input("Birinci sayı:  "))
sayi2=int(input("ikinci sayı: "))
y=1
z=1
if sayi1>sayi2:
    for x in range(1,100,1):
        if sayi1%x==0 and sayi2%x==0:
            y=y*x
            sayi1=sayi1/x
            sayi2=sayi2/x
        elif sayi1%x==0 or sayi2%x==0:
            z=z*x
if sayi2>sayi1:
    for x in range(1,sayi2,1):
        if sayi1%x==0 and sayi2%x==0:
            y=y*x
            sayi1=sayi1/x
            sayi2=sayi2/x
        elif sayi1%x==0 or sayi2%x==0:
            z=z*x
print(f"Okek: {y}, Obeb: {z}")