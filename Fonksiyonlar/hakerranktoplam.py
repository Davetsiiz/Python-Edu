def simpleArraySum(ar):
    n=int(input(print("Kaç Sayı girilecek: ")))
    to=0
    for n in range(0,n):
        ar=int(input(print(f"{n+1}. sayı giriniz.. ")))
        to=to+ar
    print(f"Toplam= {to}")

simpleArraySum(2)