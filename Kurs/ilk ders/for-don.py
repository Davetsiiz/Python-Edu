
# for x in range(1,11,2):
#     print(x)

# for x in range(1,11,):
    # print(x,".","Python")
    # print("{}.Python".format(x))
    # print(x*"p")

# x=int(input("Başlangıç sayısı giriniz: "))
# y=int(input("Bitiş sayısı giriniz: "))
# z=int(input("Artım sayısı sayısı giriniz: "))
# for h in range(x,y,z):
#     print(h)
from re import A


y=0
a=int(input("Başlangıç sayısı giriniz: "))
b=int(input("Bitiş sayısı giriniz: "))
c=int(input("Artım sayısı sayısı giriniz: "))
d=int(input("Çarpan 1: "))
e=int(input("Çarpan 2: "))
for x in range(a,b,c):
    if x%d==0 and x%e==0:
        y=y+x;
print(y)
