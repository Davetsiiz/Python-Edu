dogumyil=int(input(print("Doğum Yılınız  Giriniz")))
isim=input(print("İsminizi Giriniz"))
def yashesap(dogumyil):
    return 2022-dogumyil


def yasemek(dogumyil,isim):
    #Help Manueli için gerekli.
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize ne kadar kaldi.
    INPUT: Dogum Yili ve isim
    OUTPUT: Hesaplanan Yil 
    '''
    yas=yashesap(dogumyil)
    emeklilik=65-yas
    
    if emeklilik>0:
        print(f'Sayın {isim} emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print("Emekliliğinizi elde ettiniz.")

yasemek(dogumyil,isim)
print(help(yasemek))