# 1-100 e kadar tek sayıların toplamı.
top=0
x=0
while x<100:
    x+=1
    if x%2==0:
        continue
    top+=x
print(top)


x=0
while x<5:
    if x==2:            #2 ye geldiğinde 2 yi atlar
        continue
    elif x==4:
        break           #5 e geldiğinde döngüyü durdurur.
    print(x)
    x+=1
