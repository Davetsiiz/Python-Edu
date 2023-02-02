import random
pcsayi=random.randint(1,100)
tahminim=0
i=0
hak=4
while tahminim!=pcsayi and hak>0:
    hak-=1
    if hak==0:
        print("Hakkınız bitti...")
    elif hak>0 and tahminim==pcsayi:
        print(f"Tebrikler {i}. denemede doğru sonucu buldunuz.")
        break
    print(f"{hak} Hakkınız kaldı.")
    tahminim=int(input("1-100 arasıda sayıyı tahmin ediniz:    "))
    
    if tahminim<pcsayi:
        print("Sayı daha büyük")
    elif tahminim>pcsayi:
        print("Sayı daha küçük")
    i=i+1
    
    