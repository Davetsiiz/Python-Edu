#döngüdeki sayıları dizi içine kaydetmek
#bildiğimiz şekilde olan 
from datetime import datetime


number=[]
for x in range(10):
    number.append(x)
print(number)

#dizi içine kaydetme
numbers= [x for x in range(10)]
print(numbers)   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#örneğin her değerin karesini alacaksak 
numbers=[x**2 for x in range(10)]
print(numbers)  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#eğer sadece 3 e tam bölünenleri istiyorsak
numbers=[x**2 for x in range(10) if x%3==0]
print(numbers)  #[0, 9, 36, 81]


#yaş dizisi hesaplama
years=[1965,1966,1987,1993,1994,2015]
ages=[2022-year for year in years] 
#years dizisinin içindekiler year olur sonra döngüye girer sonra sonra 2022 yılından çıkartılır.
print(ages)


#1-10 a kadar olan sayılaarın tek ise diziye tek yazar çift ise sayıyı yazar

results=[x*1.67 if x%2==0 else 'TEK' for x in range(1,10)]  #ilk yazdırılan değişken 
print(results)

results=[(x,y,z) for x in range(3) for y in range(3) for z in range(5)]
print(results)