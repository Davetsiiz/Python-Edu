fruits = {'orange', 'apple', 'banana'}

#print(fruits[0])   indexlenemez 

for x in fruits:
    print(x)

fruits.add('cherry')   #sets komutlarında ekleme yapmak için kullanılır
print(fruits)

fruits.update(['mango','grape'])
print(fruits)

fruits.update(['mango','grape','apple'])  #apple tekrar eklendiğinde ikinciye listeye konmaz 
print(fruits)

#silmek için 3 ayrı yönteme
fruits.remove('mango')
print(fruits)
fruits.discard('apple')
print(fruits)
fruits = {'orange', 'apple', 'banana'}
fruits.pop()                 #listeden rastgele birini siler
print(fruits)

fruits.clear()
print(fruits)

    
mylist=[1,3,5,7,9,1,2,3,5]

print(mylist)
print(set(mylist))  #tekrarlayan elemanlar liste içerisinden gider

