x=5
hak=0
devam='e'

result =5 < x <10 


# and
# true,true => true
# True,false => False

result= x>5 and x<10  #5<x10 anlamına gelir yada 1 ve 2 yi aynı anda sağlaması lazım
result=(hak>0) and (devam=='e')


# or 
#true,false => true
#true,True => true
#false,false => false

result = (x > 0) or (x%2==0)    #sadece 1 ifadenin doğru olması yeterli


# not

result= not(x>0)        #sorunun cevabını tersine çevirir


#x 5-10 arasında bir çift sayı mı?
result= ((x>=5) and (x<10)and (x%2==1))
print(result)