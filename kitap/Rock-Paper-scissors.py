import random
i=0
while i==0:
    sec=("Taş","Kağıt","Makas")
    son=input(print("Çıkış için q oyuna devam etmek için bir tuşa basınızg"))
    ps=0
    ins=0

    while son!="q":
        son=input(print("Taş:0 , Kağıt:1 , Makas:2"))
        son=int(son)
        if son<0 or son>=3:
            print("Hatalı giriş.  ")
            break
        elif type(son)!=int:
            print("Hatalı giriş.  ")
            break
        else:
            sc=sec[son]
            pc=random.choice(sec)
            print(f"Sizin seçiminiz {sc}, bilgisayarın seçimi {pc}")
            
            if sc==pc:
                print("Berabere")
            elif sc==sec[0]:
                if pc==sec[1]:
                    print("Bilgisayar Kazandı")
                    ps=ps+1
                elif pc==sec[2]:
                    print("Kazandınız Tebrikler")
                    ins=ins+1
                else:
                    print("Hata")
            elif sc==sec[1]:
                if pc==sec[2]:
                    print("Bilgisayar Kazandı")
                    ps=ps+1
                elif pc==sec[0]:
                    print("Kazandınız Tebrikler")
                    ins=ins+1
            elif sc==sec[2]:
                if pc==sec[0]:
                   print("Bilgisayar Kazandı")
                   ps=ps+1
                if pc==sec[1]:
                    print("Kazandınız Tebrikler")
                    ins=ins+1                    
                    
            print(f"Durum Siz:{ins} Pc:{ps}")
