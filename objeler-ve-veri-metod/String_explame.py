website = "http://wwww.sadikturan.com"
course = "Python Kursu : Baştan sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' kaç karakterli ?
s1=len(course)
print(s1)

# 2. 'website' içinden www karakterlerini çıkart
print(website[0:7] + website[11:])

# 3. 'website' içinden com u çıkart
print(website[:-3])

# 4. 'course' içinde ilk 15 ve son 15 harfi al
print(course[:15] + course[-15:])

# 5. 'course' u tersten yazdır
print(course[::-1])   #tersten yazdırmak için -1 ile çarpıldı gibi düşünebiliriz.

# 6.
name = 'Bora'
surname = 'Yılmaz'
age = 32
job = 'mühendis'

print(f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.')
print('Benim adım {} {}, Yaşım {} ve mesleğim {}.' .format(name,surname,age,job))

# 7. 'Hello wrold' ifadesindeki w yi 'W' ile değiştir

hw= 'Hello world'
print(hw[:6]+ 'W' +hw[7:])



# 'abc' ifadesini yan yana 3 defa yazdırın
s2='abc'*3
print(s2)