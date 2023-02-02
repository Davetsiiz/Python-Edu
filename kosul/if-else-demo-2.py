# #1 girilen sayının 0-100 arasında olduğunu kontrol et
# sayi=float(input('Bir sayı giriniz:  '))
# if sayi>0 and sayi<=100:
#     print('Sayı 0-100 arasında')
# else:
#     print('Sayı 0-100 arasında değil')

# #2 girilen sayının pozitif çift sayı olup olmadığını kontrol et.
# sayi=int(input('Bir sayı giriniz:  '))
# if sayi>0 and sayi%2==0:
#     a=('Pozitif')
#     b=('Çift ')
# elif sayi>0 and sayi%2==1:
#     a=('Pozitif')
#     b=('Tek ')
# else:
#     a=('Negatif')
#     b=('')
# print(f'Sayı {a} {b}Tam Sayıdır.')

# #3 girilen mail ve parola bilgilerini kontrol ediniz.
# mails=('m@g.com')
# passws=('deneme')
# mail=input('mail giriniz: ')
# passw=input('parola giriniz: ')
# if mails==mail and passws==passw:
#     a=('Doğru')
#     b=('Doğru')
#     c=('yapabilir')
#     print(f'Mail {a}, Parola {b}. Giriş {c}.')
# elif mails==mail and passws!=passw:
#     a=('Doğru')
#     b=('Yanlış')
#     c=('yapamaz')
#     print(f'Parola {b}. Giriş {c}.')
# elif mails!=mail and passws==passw:
#     a=('Yanlış')
#     b=('Doğru')
#     c=('yapamaz')
#     print(f'Mail {a}. Giriş {c}.')
# else:
#     a=('Yanlış')
#     b=('Yanlış')
#     c=('yapamaz')
#     print(f'Mail {a}. Giriş {c}.')

# #4 girilen 3 sayıyı büyüklük olarak karşılaştır
# s1=float(input('1.sayıyı giriniz:  '))
# s2=float(input('2.sayıyı giriniz:  '))
# s3=float(input('2.sayıyı giriniz:  '))
# if s1>=s2 and s1>=s3:
#     print(f'{s1} sayısı en büyüktür.')
# elif s3>=s2 and s3>=s1:
#     print(f'{s3} sayısı en büyüktür.')
# elif s2>=s1 and s2>=s3:
#     print(f'{s2} sayısı en büyüktür.')
# else:
#     print('Hatalı giriş yaptınız.')

#  #5
# v1=float(input('1. Vize Notu:  '))
# v2=float(input('2. Vize Notu: '))
# f=float(input('Final Notu: '))
# ort=(((v1+v2)/2)*.6)+(f*0.4)

# if (ort>=50 and f>=50) or (f>=70):
#     a=('Geçer')
# else:
#     a=('Kaldı')
# print(f'Ortalama {ort}. Durum: {a}')    

#6 
boy=float(input('Boy (m): '))
kilo=float(input('Kilo (Kg): '))
en=(kilo/(boy**2))
if en>=0 and en<=18.4:
    a=('Zayıf')
elif en>=18.5 and en<=24.9:
    a=('Normal')
elif en>=25 and en<=29.9:
    a=('Fazla Kilolu')
elif en>=30:
    a=('Obez')
else:
    a=('Hesaplanamadı')
print(f'Durum: {a}. Endeks: {en}')