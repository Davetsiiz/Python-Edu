from traceback import print_tb


sayi1=float(input(" sayıyı giriniz: "))
sayi2=float(input(" sayıyı giriniz: "))
islem=str(input("İşlem seçiniz: "))
if islem==("+"):
    deg=sayi1+sayi2
    print("{} ile {} toplamı {}".format(sayi1,sayi2,deg))
    print(sayi1+sayi2)
elif islem==("-"):
    deg=sayi1-sayi2
    print("{} ile {} farkı {}".format(sayi1,sayi2,deg))
    print(sayi1-sayi2)
elif islem==("*"):
    deg=sayi1*sayi2
    print("{} ile {} çarpımı {}".format(sayi1,sayi2,deg))
    print(sayi1*sayi2)
elif islem==("/"):
    deg=sayi1/sayi2
    print("{} ile {} bölümü {}".format(sayi1,sayi2,deg))
    print(sayi1/sayi2)
else:
    print("Hatalı veri")