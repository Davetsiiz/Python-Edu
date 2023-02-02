name = 'Murat'
surname = 'EREN'
age = 30

print("\n")

greeting = 'My name is '+ name + " " + surname + " and \nI am " + str(age) + " years old." #\n yeni satır oluşturur bu cümleyi ikiye böler
print(greeting)

print("\n")

print('My name is '+ name + " " + surname + " and \nI am " + str(age) + " years old." ) #\n yeni satır oluşturur bu cümleyi ikiye böler.

print("\n")

print(greeting[0])      #cümlenin ilk harfini yazdırır
print(greeting[1])      #ikinci harf yazdırılır

#print(len(greeting))    #str ifadenin kaç karakterli olduğunu söyler
length = len(greeting)
print(greeting[length-1])
print(greeting[-1])     #str ifadenin son karakterini söyler üstteki satırla aynı görevi görür

print(greeting[3:40])   #str ifadenin 4. karakterinden 41. karakterine kadar yazar (sayma 0 dan başladığı için +1 ile ifade edilir)
print(greeting[3:])     #str ifadenin 4. karakterinden başlkar sonra kadar yazar
print(greeting[:16])    #str ifadenin 17. karakterine kadar yazar
print(greeting[3:44:3]) #str ifadenin 4. karakterinden 45. karakterine kadar yazar ama 3 atlama ile yazar

