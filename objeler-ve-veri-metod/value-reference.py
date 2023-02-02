
#value type => string ve number bunların içindedir
x = 5
y = 25

x=y     #y nin değeri x e aktarıldı
y=10    #y değeri değiştirildi y deki değişiklik x i etkilemedi
        #sonuç 25 10 şeklinde çıkar
        
#print(x,y)

#reference type => list ve class 
a=["apple","banana"]
b=["apple","banana"]

a = b  #b nin bilgileri a nın içine atıldı #adresler biribirine eşitleniyor 


b[0]= "grape"   #b nin üzerindeki değişiklik a yı etkiler
                #adreslemeler aynı olduğu için değişiklikler birbirini etkiler
                

print(a,b)

