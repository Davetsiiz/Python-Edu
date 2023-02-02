

student={
    '120':{
        'name': 'Ali',
        'surname': 'Yılmaz',
        'phone': '5320000001'
    },
    '125':{
        'name': 'Can',
        'surname': 'Korkamaz',
        'phone': '5320000002'
    },
    '128':{
        'name': 'Volkan',
        'surname': 'Yükselen',
        'phone': '5320000003'
    }

}
print(student[input("Okul Numarası Giriniz:   ")])


ogrenci={}
number=input('Okul No:  ')
isim= input('İsim : ')
soyad=input('Soyad :')
telefon=input('Telefon numarası: ')

ogrenci[number]={
    'ad': isim,
    'soyad':soyad,
    'telefon' : telefon
}
print(ogrenci)
print(ogrenci[input("Okul Numarası Giriniz:   ")])

for i in student:
    print(i)
else:
    print("böyle bir  şey yok")

