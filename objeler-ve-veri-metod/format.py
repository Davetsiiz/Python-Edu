name = "Murat"
surname = "EREN"
age = 36
print("My name is {} {}" .format(name, surname))

print("My name is {1} {0}" .format(name, surname))   #indek numaralrı formattaki sıraya göre yazılır. 0 yerine 1 yazılırsa soyad ad yer değiştirmiş olur
print("My name is {n} {s}" .format(n=name, s=surname))  #değişken atayarak süslü parantez içine değişkenleri yazarsak yine aynı şeye erişiriz


print("My name is {} {} and I'm {} years old. " .format(name, surname, 36))   #36 yerine değişken atanabilir yada '36' yazılabilir.

result = 200/850

print("The result is {r:1.4}" .format(r=result))   #r:1.4  1 virgül öncesi kaç karakterlik genişlik bırkacağını gösterir olması gerekiyor onu gösterir 4 bilgisi toplam karakter uzunluğunu verir


print(f"My name is {name} {surname} and I'm {age} years old. " )  #fstring formatı 
