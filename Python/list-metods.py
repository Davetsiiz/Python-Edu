numbers =[1,10,223,456,45]
letters = ['a', 'g', 'b', 'f', 'z', 'm']
val=min(numbers)
print(val)
mval=max(numbers)
print(mval)
milet=min(letters)
malet=max(letters)
print(milet)
print(malet)

val=numbers[3:6]
print(val)


numbers[4]=40
print(numbers)

numbers.append(10) # en sona ekler
print(numbers)

numbers.insert(3,31) #3. indekse ekler
print(numbers)

numbers.insert(-1,67)  #ensondan bir öncekine ekler en sona eklemek için append kullanılmalı
print(numbers)

numbers.pop(3)   #3. indeksteki rakamı siler
print(numbers)

numbers.remove(40)   #40 rakamını siler
print(numbers)

numbers.sort()   # küçükten büyüğe sıralama yapar
print(numbers)

letters.sort()
print(letters)

numbers.reverse()    #diziyi tersten yazar
print(numbers)

print(numbers.count(10))  #dizi içinde 10 sayısı kaç tane var.

numbers.clear()    #temizleme komutu 
print(numbers)



