from cmath import pi
r = float(input("Yarı Çap : "))
dA = pi*(r**2)
dC = 2*pi*r
print('Daire Alanı:' + ' ' + str(dA) )      #str birlşetirmede sadece str bilgi kullanılmalı
print('Daire Çevresi:' + ' ' + str(dC) )    
print("Alan: {r:2.2}".format(r=dA))             #çevirme işlemini yapmana gerek kalmıyor
print("Çevre: ", dC)
