#bir kelimeyi istediğini kadar yadar yazan fonskiyon

# def yazdir(kelime1,adet):
#     print(kelime1*adet)
# yazdir("Merhaba\n",6)


# kelime=str(input(print("Yazdırılacak kelime:  ")))
# sayi=int(input(print("Kaç kez yazdırılacak:  ")))
# def q1(kelime,sayi):
#     for i in range(0,sayi):
#         print(kelime)

# q1(kelime,sayi)


#kendine gönderilen sınırsız sayıdaki parametreyi listeye yazan fonsksiyon

# def lister(*params):  #* işareti sonsuz olması için
#     liste=[]
    
#     for param in params:
#         liste.append(param)
#     return liste
# result= lister(10,20,30,'merhaba')
# print(result)

#gönderilen 2 sayı arasındaki tüm asalsayıları bulun

def asal(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1 :
            for i in range(2,sayi):
                if (sayi %i==0):
                    break
            else:
                print(sayi)
sayi1=int(input(print("sayi 1:")))
sayi2=int(input(print("sayi 2:")))
asal(sayi1,sayi2)