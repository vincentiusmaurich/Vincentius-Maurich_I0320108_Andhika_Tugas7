nama = input("Masukkan nama lengkap Anda : ").lower()

#Fungsi String 1 = huruf kapital di seluruh string
kapital = f"Selamat datang, {nama.upper()}!"

#Fungsi String 2 = center
tengah = kapital.center(100,"-")
print(tengah)

#Fungsi String 3 = menghitung jumlah huruf
print("Jumlah huruf vokal pada nama Anda")
print("'a' =", nama.count('a'), "'i' =", nama.count('i'), "'u' =", nama.count('u'), "'e' =", nama.count('e'), "'o' =", nama.count('o'))