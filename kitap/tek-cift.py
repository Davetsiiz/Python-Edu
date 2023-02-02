sayi=int(input("Bir sayı giriniz: "))
kalan=sayi%2

if kalan==1:
    print("Tek Sayi")
elif kalan==0:
    print("Çift Sayi")
else:
    print("Yanlış Giriş")
