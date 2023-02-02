mails=('m@g.com')
passws=('deneme')



#1 sayı 0-100 arasında mı ?
# sayi=float(input('Sayı giriniz: '))
# result= ((sayi>=0)and (sayi<100))

# 2 sayının pozitif çif sayı olup olmadığı
# sayi=int(input('Sayı giriniz: '))
# result= ((sayi>=0)and (sayi%2==0))

# 3 email ve parola kontrolü
# mail=input('mail giriniz: ')
# passw=input('parola giriniz: ')
# result= ((mail==mails) and (passw==passws))

# 4 girilen 3 sayıyı büyüklük olarak karşılaştır


#  5 
# v1=float(input('1. Vize Notu:  '))
# v2=float(input('2. Vize Notu: '))
# f=float(input('Final Notu: '))
# ort=(((v1+v2)/2)*.6)+(f*0.4)
# result=((ort>=50) and (f>=50)) or (f>=70)
# print(f'Ortalama: {ort} Geçme durumu: {result}')

# 6 
boy=float(input('Boy (m): '))
kilo=float(input('Kilo (kg): '))
en=(kilo/(boy**2))
result=en 
r1= en>=0 and en<=18.4
print(f'Zayıf: {r1}')
r2= en>=18.5 and en<=24.9
print(f'Normal: {r2}')
r3= en>=25 and en<=29.9
print(f'Fazla Kilolu: {r3}')
r4= en>=30 
print(f'obez: {r4}')

print(f'Sonuç : {result}')