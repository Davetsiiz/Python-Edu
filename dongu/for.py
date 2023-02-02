numbers=[1,2,3,4,5]

for i in numbers: #i değişkeni indis numarası gibi çalışır.
    print(i)        # eğer i yi print edersek liste içindekileri yazdırır
    print('Hello')  #liste içindeki sayılar kadar yazdırır.

names = ['Murat','Nesli','Emre']
for name in names:
    print(f'My Name is {name}')
    
n='murat eren'
for m in n:
    print(m)        #n içindeki tüm harflar tek tek yazdırılır.

tuple=[(1,2),(4,5), (8,6)]      #tuple için

for a,b in tuple:
    print(a)
    print(a,b)

d={'k1':1, 'k2':2, 'k3':3}      #dictionary
for item in d.items():
    print(item)

for key,value in d.items():
    print(key,value) 