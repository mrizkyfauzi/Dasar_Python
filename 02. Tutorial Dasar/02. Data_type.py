angka = [10, 3.14, 1000000000000000000000, 10+5j]
karakter = "A"
kalimat = " Begini amat hidup :D"
is_admin = True 
is_member = False 
daftar_angka = [1, 2, 3]
daftar_huruf = ('a','b','c')
data_orang = {'nama':'michael' , 'country':'Paris', 'Telp':2223}

print(f"{angka[0]} Class INT")
print(f"{angka[1]} Class Float")
print(f"{angka[2]} Class INT")
print(f"{angka[3]} Class Complex")
print(f"{is_admin} , {is_member} Class Boolean, ", type(is_admin))
print(f"{daftar_huruf} Class Tuple" ) 
print (f"{data_orang} Class Dictionary")


# Belajar Casting
# Merubah dari satu tipe ke tipe lain

angka_int = int(angka[1])
angka_str = str(angka[1])
angka_bool = bool(angka[1])
print("data = ", angka_int, ",type = ", type(angka_int))
print("data = ", angka_str, ",type = ", type(angka_str))
print("data = ", angka_bool, ",type = ", type(angka_bool))