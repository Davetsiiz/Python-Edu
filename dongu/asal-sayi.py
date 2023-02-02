sayi=int(input(print("Bir Sayı giriniz.")))
ami= True
if sayi==1:
    print("1 sayısı asal değil...")

for x in range(2,sayi):
    if (sayi % x==0):
        ami= False
        break

if ami==True:
    print("Sayı Asaldır...")
elif ami==False:
    print("Sayı Asal Değildir...")