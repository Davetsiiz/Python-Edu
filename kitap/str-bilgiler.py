
from platform import platform


print("selam""ben""murat")          #selambenmurat
print("selam","ben","murat")        #selam ben murat
print("selam"+"ben"+"murat")        #selambenmurat

print("www","murat","com", sep=".") #www.murat.com
print("selam","ben","murat",sep="-")    #selam-ben-murat
print(*"murat")                     #m u r a t
print(*"murat",sep="/")             #m/u/r/a/t
print(*"EMRE",*"MURAT",*"EREN", sep="*")    #E*M*R*E*M*U*R*A*T*E*R*E*N
print("Emre","Murat","Eren",sep="\n")       #Alt alta yazar

print('Murat\'ın evi')              #Murat'ın evi
print("Selam Ben Murat", end=".\n")   #en sona nokta koyar ve imleci en sonda bekletir.

#ad=input(print("İsim"))
#soyad=input(print("Soyad"))
#print(f"{ad=}, {soyad=}")           #ad="isim", soyad="soyisim"


fiyat="#3,1471$"
ilk,*orta,son=fiyat
print(f"{ilk=},{orta=},{son=}")     #ilk='#',orta=['3', ',', '1', '4', '7', '1'],son='$'
orta=(print(*orta,sep=""))          #3,1471
 
kelime="Emre-Murat-Eren"
for i in range(0,len(kelime)):
    if kelime[i]!="-":
        kelime[i]
        print(kelime[i],end="")
    elif kelime[i]=="-":
        print("",end=" ")

print("\n"+kelime[:len(kelime):2])

platform.uname()
