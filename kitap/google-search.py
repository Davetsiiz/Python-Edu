import webbrowser

sorgu=input(print("Aradığınız kelimeyi giriniz: \n"))
adres=f"https://www.google.com/seach?q={sorgu}"

webbrowser.open(adres)

kelime=input(print("Aradığınız kelimeyi yazınız:    \n"))
kadres=f"https://tureng.com/en/turkish-english/{kelime}"

webbrowser.open(kadres)