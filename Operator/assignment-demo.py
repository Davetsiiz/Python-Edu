x,y,z=2,5,10
numbers=1,5,7,10,6

# # 1 kullanıcıdan aldığınız iki sayının çarpımı ile x,y,z toplamının farkını yazdır
d1=int(input("İlk sayıyı giriniz: "))    #int değere çevirmeyi unutma
d2=int(input("İkinci sayıyı giriniz: "))
d3=d1*d2
d4=x+y+z
d5=d3-d4
print("Sonuç: {}".format(d5))
print(f'Sonuç: {d5}')

# 2 y' nin x'e kalansız bölümü nedir
# print(y//x)
# 3 (x,y,z) toplamının mod 3 nedir
# d6=x+y+z
# d6%=3
# print(d6)
# 4 y nin x inci kuvveti
# y**=x
# print(y)
# 5 x,*y,z=numbers işlemine göre z nin 2 inci kuvveti nedir?
# x,*y,z=numbers
# print(x,y,z)
# z**=3
# print(z)
# 6 x,*y,z=numbers işlemine göre y nin değerler toplamı nedir?
# x,*y,z=numbers
# y=y[0]+y[1]+y[2]
# print(y)
