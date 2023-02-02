# 1. Liste oluşturma
lc = ['Bmw', 'Mercedes','Opel','Mazda']
print(lc)

# 2. Liste eleman sayısı
lclen = len(lc)
print(lclen)

# 3. Listenin ilk ve son elemanı nedir?
print(lc[0],lc[-1])
      
# 4. Mazda değerini toyota ile değiştir.
lc[3] = 'Toyota'
print(lc)

# 5. Mercedes listenin bir elemanı mı?
onay = 'Mercedes' in lc  #liste içinde 'Mercedes' elemanı bulunuyor mu
print(onay)

lc = ['Bmw', 'Mercedes','Opel','Mazda']
md = lc.index('Mercedes')   #hangi eleman 'Mercedes' tir
print(md)


# 6. List -2 nedir
print(lc[-2])

# 7. ilk üç eleman nedir?
print(lc[:3])

# 8. listenin son iki elemanı yerine 'Toyota' ve 'Renault' yaz
lc[-2:]=['Toyota','Renault']    #liste için
print(lc)

# alternatif yol tek tek eklemek
lc = ['Bmw', 'Mercedes','Opel','Mazda']
lc.pop(-1)      #özel pozisyondaki elementi siler 
lc.pop(-1)

lc.insert(3,'Toyota')  #belli bir pozisyona eleman ekler 
lc.insert(4,'Renault')
print(lc)

# 9. Listenin Sonuna 'Audi' ve 'Nissan' elemanlarını ekle

yenilc = ['Audi','Nissan']
lc.extend(yenilc)
print(lc)

# 10. Listenin son elemanını silin 
lc = ['Bmw', 'Mercedes','Opel','Mazda']
lc.pop(-1)      #özel pozisyondaki elementi siler 
print(lc)

lc = ['Bmw', 'Mercedes','Opel','Mazda']
del lc[-1]
print(lc)


# 11. listedeki elemanları tersten yazdırın
lc = ['Bmw', 'Mercedes','Opel','Mazda']
lc.reverse()    #listeyi tersten yazdırır 
print(lc)

#12.  Listeyi oluştur

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]
print(studentA,studentB,studentC)

#13 elelmanları yazdırın
a1= studentA[0]
print(a1)
a2 = studentA[1]
print(a2)
a3=studentA[3][1]
print(a3)



