sy=[1,3,5,7,9,12,19,21]

# 1.sayılar listesini ekrana while ile yazdır
# i=len(sy)
# sa=0
# while i>0:
#     print(sy[sa])
#     sa+=1
#     i-=1

# 2.Başlangıç ve bitiş değerlerini alıp aradaki tüm tek sayıları yazdırın
# s1=int(input('Başlangıç sayısı giriniz: '))
# s2=int(input('Bitiş sayısı giriniz: '))
# if s1>s2:
#     print('Hatalı giriş yaptınız.')
# else:
#     while s2>s1:            #s2>s1 olduğu sürece yazdır
#         if s1%2==1:
#             print(s1)
#         s1+=1

# 3. 1-100 arasındaki sayıları azalan şeklinde yazınız.
# s1=100

# while s1>2:
#     s1-=1
#     print(s1)

# 4.Kullanıcıdan alacağınız 5 sayıyı büyükten küçüğe yazınız
# i=1
# ls=[]
# while i<=5:
#     s1=int(input(f'{i}. sayı giriniz: '))
#     ls.append(s1)
#     i+=1
# ls.sort()
# ls.reverse()
# print(ls)
# i=len(ls)
# sa=0
# while i>0:
#     print(ls[sa])
#     sa+=1
#     i-=1


# 5. Kullanıcıdan alacağınız sınırsız ürün bilgisi ile ürünleri liste içinde saklayınız.
sayi=int(input('Ürün miktarı giriniz: '))
ub=[]
while sayi>0:
    name=input('Ürün ismi giriniz:')
    price=float(input('Ürün fiyatı giriniz:'))
    ub.append({
        'name':name,
        'price': price
    })
    sayi-=1
for urun in ub:         #urun burda sayaç görevi görür
    print(f'Ürünün adı:{urun["name"]} Ürünün fiyatı: {urun["price"]}')


