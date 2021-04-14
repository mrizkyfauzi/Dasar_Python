#string
nama = "Fauzi"
format_str = f"Hello {nama}"
print(format_str)


# Boolean
boolean = False
format_bool = f"boolean = {boolean}"
print(format_bool)

# Angka
Angka = 2005.5
format_angka = f"Angka = {Angka}"
print(format_angka)

# Bulat
Bulat = 15
format_bulat = f"Bilangan Bulat = {Bulat:d}"
print(format_bulat)

# Ribuan dengan ordo
angka = 20000000
format_ribuan = f"ribuan = {angka:,}" 
print(format_ribuan)

# Bilangan Desimal 
Angka = 2005.5423
format_angka = f"desimal = {Angka:.3f}"
print(format_angka)

# Leading Zero 
Angka = 2005.5423
format_angka = f"Leading Zero = {Angka:09.3f}"
print(format_angka)

# tand + dan -

angka_minus = -10
angka_plus = 10
format_minus = f" Minus = {angka_minus}"
format_plus = f" Plus = {angka_plus:+d}"

print(format_minus)
print(format_plus)