# 1-100 e kadar sayıları yazdır
# x= 1
# top=0
# while x<=10:
#     if x%2==0:
#         print(x)
#         top+=x
#     x+=1
    
# print('bitti....')
# print(top)


# girilen sayının faktöriyeli
# sr=int(input('Bir sayı giriniz: '))
# top=1
# while sr>0:
#     top=top*sr
#     sr-=1
# print(top)

# girilen paranın her hafta % büyümesi
# sayi=float(input('Para miktarı giriniz: '))
# hf=float(input('Hafta sayısı giriniz: '))
# bm=float(input('%  ' 'Büyüme miktarı:'))
# bm=bm/100 
# top=0
# while hf>0:
#     sayi=(sayi*bm)+sayi
#     hf-=1
# print(sayi)


#
name=''   #false
while not name.strip():     #name ifadesi sürekli false olacağı için not ile true değeri veririz
                            #strip() kullanma sebebi boşluk girilen isimlerin önüne geçmek 
    name=input('İsminizi giriniz:')
print(f'Merhaba, {name}')
