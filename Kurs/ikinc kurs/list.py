#serkan özargın
soyad="eren"
soyad=soyad.upper()
cevap=(input(f"Soyadınızın ilk üç harfini  giriniz: ")).upper()

soyisimharflari=soyad[0:3]
print(soyisimharflari)


if cevap==soyisimharflari:
    print("Doğru")
else:
    print("Yanlış")