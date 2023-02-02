vize=int(input("vize notu giriniz:  "))
final=int(input("final notu giriniz:  "))
ort=float((vize+final)/2)
print("Ortalama:  ", ort)
if ort>49:
    print("geçti")
    
elif ort<50:
    print("Kaldı")


if ort<45 and ort>=0:
    print("Not:", "FF")
    hn=str("FF")
elif ort>=45 and ort<55:
    print("Not:", "DD")
    hn=str("DD")
elif ort>=55 and ort<70:
    print("Not:", "CC")
    hn=str("CC")
elif ort>=70 and ort<85:
    print("Not:", "BB")
    hn=str("BB")
elif ort>=85 and ort<=100:
    print("Not:", "AA")
    hn=str("AA")
else:
    print("Hatalı Giriş yaptınız")

print(f"Ortalama: {ort}, Harf Notu: {hn}")

