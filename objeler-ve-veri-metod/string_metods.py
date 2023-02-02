message = 'Hello There. My name is Murat Eren.'

print(message)

message = message.upper()   #bütün karakterleri büyük yapar
print(message)

message = message.lower()   #bütün karakterleri küçük yapar
print(message)

message = message.title()   #cümleyi başlık formatında yazar
print(message)

message = message.capitalize()   #sadece ilk harf büyük olur 
print(message)

message = ' Hello There. My name is Murat Eren. '
message = message.strip()        #baştaki ve sondaki boşlukları siler 
print(message)

message = message.split()        #her kelimeyi bölümlere ayırır (dizi oluşturur)
print(message)
print(message[3])               #3. indekteki kelimeyi verir yani 'name' yazdırır
message = ' '.join(message)     #böldüklerimi birleştirir. tırnaklar arası boşluk bıraktık ki eski hali gib olsun.
print(message)


message = 'Hello There. My name is Murat Eren.'
message = message.split('.')        #noktadan itibaren böler. cümleleri bölmüş olur
print(message)
print(message[1])

message = 'Hello There. My name is Murat Eren.'
index =message.find('Murat')            #Murat kelimesinin başladığı indeksi bulur
print(index)

isFound = message.startswith('H')   #mesaj H harfi ile mi başlıyor başlıyor ise True cevabı verir.
print(isFound)

isFound = message.endswith('.')   #mesaj . harfi ile mi bitiyor bitiyorsa True cevabı verir.
print(isFound)

message=message.replace('Murat','Neslihan')     #Murat bilgisini arar ve yerine Neslihan yazar.
print(message)

message=message.center(50)          #50 karakterlik alan oluşturur ve yazıyı tam ortalar.
print(message)

message = 'Hello There. My name is Murat Eren.'
message=message.center(50,'*')          #50 karakterlik alan oluşturur ve yazıyı tam ortalar. Boşluk yerine yıldız yazdırır.
print(message)