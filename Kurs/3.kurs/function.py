

# import turtle
# def kare():
#     turtle.home()

#     for x in range(4):
#         turtle.forward(100)
#         turtle.left(90)
# kare()

# import turtle
# def renkkare(renk):
#     turtle.pencolor(renk)
#     turtle.home
#     for x in range(4):
#         turtle.forward(100)
#         turtle.left(90)

# renkkare("purple")


#faktoriyel
def faktor():
    sayi=int(input(print("Sayı giriniz: ")))
    to=1
    if sayi<0:
        print("Negatif sayı girdiniz.")
    elif sayi==0:
        print("Değer= 1 ")
    elif sayi>0:
        for x in range(1,sayi+1,1):
            to=to*x
        print(f"Değer= {to}")
    else:
        print("Hatalı giriş")

faktor()