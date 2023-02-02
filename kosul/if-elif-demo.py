# 1
# isim= input('İsim:')
# yas= float(input('Yaş: '))
# eg= input('Eğitim: ')
# if (yas>=18) and (eg.lower()==('lise')or eg.lower()==('üniversite')):
#     a=('alabilir.')
#     b=('')
#     print(f'{isim} adlı kişi {b} ehliyet {a}')
# elif (yas<18):
#     if eg.lower()=='lise' or eg.lower()=='üniversite':
#         a=('alamaz.')
#         b=('yaşından dolayı')
#         print(f'{isim} adlı kişi {b} ehliyet {a}')
#     else:
#         a=('alamaz.')
#         b=('yaşından ve eğitim durumundan dolayı')
#         print(f'{isim} adlı kişi {b} ehliyet {a}')
# else:
#     print('Hatalı Giriş Yaptınız')
        
# 2
# v1=float(input('1.Sınav: '))
# v2=float(input('2.Sınav: '))
# s1=float(input('1.Sözlü: '))
# ort=(v1+v2+s1)/3
# if ort>=0 and ort<=25:
#     print('Not: 0 ')
# elif ort>25 and ort<45:
#         print('Not: 1 ')
# elif ort>=45 and ort<55:
#         print('Not: 2 ')
# elif ort>=55 and ort<70:
#         print('Not: 3 ')
# elif ort>=70 and ort<85:
#         print('Not: 4 ')
# elif ort>=85 and ort<=100:
#         print('Not: 5 ')
# else:
#     print('Yanlış Değer Girdiniz')

# 3 trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdaki bilgilere göre hesaplayınız.
#1.Bakım 1.yıl
#2.Bakım 2.yıl
#3.Bakım 3.yıl

#1.yol
# my_date=int(input('aracınız kaç gündür trafikte:'))
# if my_date<=365:
#      print('1. Bakım')
# elif my_date>365 and my_date<=365*2:
#      print('2. Bakım')
# elif my_date>365*2 and my_date<=365*3:
#      print('3. Bakım')
# else:
#      print('Yanlış Bilgi')

#2.yol
# from datetime import date
# import datetime
# my_date=input('Tarih Giriniz (Yıl/Ay/Gün): ')
# my_date=my_date.split('/')
# print(my_date[0])
# print(my_date[1])
# print(my_date[2])
# trc=datetime.datetime(int(my_date[0]),int(my_date[1]),int(my_date[2]))
# print(trc)
# simdi=datetime.datetime.now()    #şu anki tarihi ve saati verir
# sr=(simdi-trc).days
# print(sr)

# if sr<=365:
#      print('1. Bakım')
# elif sr>365 and sr<=365*2:
#      print('2. Bakım')
# elif sr>365*2 and sr<=365*3:
#      print('3. Bakım')
# else:
#      print('Yanlış Bilgi')
 
 
 
# today= date.today()
# print("date",today)