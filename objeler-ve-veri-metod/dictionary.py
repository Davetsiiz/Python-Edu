# #key - value olarak çalılşır
# # mesela 41>kocaeli 34>istanbul şeklinde çalışır

# # sehirler = ['kocaeli','istanbul']
# # plaka = [41,34]

# # print(plaka[sehirler.index('kocaeli')])
# # Sadece list metodu ile yapılanlar bunlar sıralar aynı olmalı

# # x= {key : value, key2 : value2 } şeklinde dictionary yazılır
# plaka = {'kocaeli' : 41, 'istanbul': 34}

# print(plaka['istanbul'])
# print(plaka['kocaeli'])

# #yeni value ekleme 
# plaka['kırklareli']=39  #yeni
# plaka['kocaeli']=41.5   #değişim
# print(plaka)

users ={
     'Murat Eren'    :{
         'age':27,
         'roles':['admin','users'],
         'email':'asd@gmail.com',
         'address'  : 'Bursa',
         'phone'    : '02886154037'

     },
     'Neslihan Eren' :{
         'age':28,
         'roles':['admin','users'],
         'email':'asssd@gmail.com',
         'address': 'İstanbul',
         'phone': '028824567892'

     },
     'Bade Eren'     :{
         'age'  :34,

         'roles':['users'],
         'email':'ababab@gmail.com',
         'address'  : 'Sweeden',
         'phone'    : '09886626262'

     },
     'Ahmet Eren'    :{
         'age'  :90,
         'email':'yok',
         'roles':['users'],
         'address'  : 'Kırklareli',
         'phone'    : '02824187654'

     }

}
print(users['Murat Eren'])
print(users['Murat Eren']['age'])
print(users['Murat Eren']['roles'])
print(users['Murat Eren']['email'])
print(users['Murat Eren']['address'])
print(users['Murat Eren']['phone'])
print(users['Neslihan Eren'])
print(users['Bade Eren'])
print(users['Ahmet Eren'])
