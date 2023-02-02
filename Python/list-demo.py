names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1. liste sonuna isim ekleyin
# names.append('Cenk')

# 2. liste başına isim ekleyin
# names.insert(0,'Sena')

# 3. 'Deniz' ismini listeden siliniz
# names.remove('Deniz')

# 4. 'Deniz' elementinin indeksi nedir?
# print(names.index('Deniz'))

# 5. 'Ali' listenin bir elemanı mıdır?
# print(names.count('Ali'))

# 6. elemanları tersten yazdırın
# names.reverse()

# 7. liste elemanlarını alfabetik olarak sıralayın
# names.sort()

# 8.years listesini rakamsal olrak sıralayın
# years.sort()

# 9. str karakter dizisini listeye çevirin
# str= 'Chevrolet,Dacia'
# result= str.split(',')
# print(result)


#  10. yearsın en büyük ve en küçük elemanları nelerdir.
# print(min(years) , max(years))

# 11. years dizisinde kaç tane 1998 vardır
# print(years.count(1998))

# 12. years listesini siliniz
# years.clear()

# 13. Kullanıcıdan alacağınız 3 tane marka bilgisini listede saklayınız
markalar =[]

marka = input("Marka :  ")
markalar.append(marka)
marka = input("Marka :  ")
markalar.append(marka)
marka = input("Marka :  ")
markalar.append(marka)

print(markalar)


print(names)
print(years)
