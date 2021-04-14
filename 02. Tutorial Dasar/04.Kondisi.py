print("-----------------------------")
print("      If & Else")
print("-----------------------------")

nilai = 85
if nilai > 75 :
    print(" Maka Anda Lulus")
else:
    print("maka Anda Tidak lulus")

print("-----------------------------")
print("      If & Elif")
print("-----------------------------")

nilai = 50
if nilai > 85:
    print(" Anda Mendapatkan Nilai Sempurna")
elif nilai >= 90:
    print("Anda Mendapatkan Nilai Paling Bagus")
else:
    print("Nilai Anda Jelek")

print("-----------------------------")
print("      Nested IF")
print("-----------------------------")

print("Masukkan Data =") 
print("Nama Siswa :")
Nama = input()
print("Nilai Siswa :")
Nilai = int(input())

if Nilai > 80:
    print(f"Selamat, Kamu {Nama} Mendapatkan Nilai A")
    if Nilai > 95:
        print(f"Kamu {Nama} mendapat tambahan bonus voucer Belanja")
    elif Nilai == 100:
        print(f"Kamu {Nama} Mendapatkan tambahan Bonus Voucer Jalan- Jalan ")
elif Nilai > 70:
    print(f"Selamat, Kamu {Nama} Mendapat Nilai B")
elif Nilai > 55:
    print(f"Kamu {Nama} Mendapat Nilai C")
else:
    print(f"Kamu {Nama} Perlu Remedial")


print("-----------------------------")
print("      Ternery Operator")
print("-----------------------------")

total_belanja_1 = 250000
diskon_1 = True if total_belanja_1 > 200000 else False
print (diskon_1)

total_belanja_2 = 50000
diskon_2 = True if total_belanja_2 > 200000 else False
print (diskon_2)

total_belanja_3 = 100000
diskon_3 = True if total_belanja_3 > 200000 else False
print (diskon_3)
