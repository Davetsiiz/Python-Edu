ma1 = 5000
ma2 = 4000
vergi = 0.27

print(5000-(5000*0.27))
print(ma1 - (ma1*vergi))
print(ma2-(ma2*vergi))

# Değişken tanımlama kuralları

# sayısal ifade ile başlayamaz

number1 = 20
print(number1)
number1 = 10
print(number1)

number1 +=20
print(number1)


# BÜyük küçük harf duyarlılığı vardır

Age = 20
age = 30
AGE = 10
print(Age)
print(age)
print(AGE)


#   Türkçe karakter kullanmayın

Yas=10

# Metinsel ifade saklama

name = "Şarkı"          # string
print(name)
x = 1                   # in
y = 2.3                 # float
# Evet yada hayır değeri saklayacaksak
isName = True           #bool   
isSurname = False       #bool

# toplu tanımlama yapılabilir
a, b, isim, soyisim =(10, 2.4, 'murat', ' eren')
print(a+b)
print(isim+ soyisim)


