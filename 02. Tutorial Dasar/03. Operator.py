
print("-----------------------------")
print("      Arithmetic Operator")
print("-----------------------------")
print("Masukkan Nilai X :  ") 
X = int(input())
print("Masukkan Nilai Y : ") 
Y = int(input())


Penjumlahan = X + Y
Pengurangan = X - Y
Pembagian = X / Y 
Modulus = X % Y 
Pangkat = X ** Y
Pembagian_Bulat = X // Y 

Sama_dengan = X == Y
Tidak_sama_dengan = X!= Y
Lebih_dari = X > Y
Kurang_dari = X < Y
Lebih_sama_dengan = X >= Y
Kurang_sama_dengan = X <= Y

Dan = Sama_dengan and Tidak_sama_dengan
Atau = Sama_dengan or Tidak_sama_dengan







print("-----------------------------")
print(f"{X} + {Y} = {Penjumlahan}, Operator Penjumlahan")
print("-----------------------------")
print(f"{X} - {Y} = {Pengurangan}, Operator Pengurangan")
print("-----------------------------")
print(f"{X} / {Y} = {Pembagian}, Operator Pembagian")
print("-----------------------------")
print(f"{X} % {Y} = {Modulus}, Operator Modulus")
print("-----------------------------")
print(f"{X} ** {Y} = {Pangkat}, Operator Pangkat")
print("-----------------------------")
print(f"{X} // {Y} = {Pembagian_Bulat}, Operator Pembagian Bulat")

print("")
print("")
print("-----------------------------")
print("     Comparison Operator")
print("-----------------------------")
print("Masukkan Nilai X :  ") 
X = int(input())
print("Masukkan Nilai Y : ") 
Y = int(input())

# Lebih dari >
hasil = X > 3
print(X,'>',3,'=',hasil)
hasil = Y > 3
print(Y,'>',3,'=',hasil)

# Kurang dari 
hasil = X < 3
print(X,'<',3,'=',hasil)
hasil = Y < 3
print(Y,'<',3,'=',hasil)

# sama dengan 
hasil = X == 3
print(X,'==',3,'=',hasil)
hasil = Y == 3
print(Y,'==',3,'=',hasil)

# tidak sama dengan 
hasil = X != 3
print(X,'!=',3,'=',hasil)
hasil = Y != 3
print(Y,'!=',3,'=',hasil)

# is sebagai komparasi object
X = 5
y = 5
print('nilai x = ',X, ', id = ', hex(id(X)))
print('nilai y = ',y, ', id = ', hex(id(y)))
hasil = X is y
print('X is Y =', hasil)

print("")
print("")
print("-----------------------------")
print("     Logical Operator")
print("-----------------------------")
print("Masukkan Nilai X :  ") 
X = int(input())
print("Masukkan Nilai Y : ") 
Y = int(input())
print("-----------------------------")
print(f"{X} == {Y} = {Sama_dengan} | and {X} != {Y} = {Tidak_sama_dengan} || {Dan} Operator And")
print("-----------------------------")
print(f"{X} == {Y} = {Sama_dengan} | or {X} != {Y} = {Tidak_sama_dengan} || {Atau} Operator Or")

print("---------- NOT ----------")
a = True
c = not a
print("data Boolean = ", a)
print('------------------- NOT')
print('data c =' ,c )

print("---------- OR ----------") #Jika salah satu bernilai true maka dia akan true
a = True
b = False
c = c or b
print(a, "OR",b, '=',c)

a = False
b = True
c = a or b
print(a, "OR",b, '=',c)

a = True
b = True
c = a or b
print(a, "OR",b, '=',c)

print("========= AND ===========") #Jika ada true maka akan false
a = True
b = False
c = a and b
print(a, "AND",b, '=',c)

a = False
b = True
c = a and b
print(a, "AND",b, '=',c)

a = True
b = True
c = a and b
print(a, "AND",b, '=',c)

print("========= XOR ===========") # Akan true jika salah 1 true
a = True
b = False
c = a ^ b
print(a, "XOR",b, '=',c)

a = False
b = True
c = a ^ b
print(a, "XOR",b, '=',c)

a = True
b = True
c = a ^ b
print(a, "XOR",b, '=',c)

print("-----------------------------")

print("")
print("")
print("-----------------------------")
print("     Assignment Operator")
print("-----------------------------")

print("Masukkan Nilai Bilangan : ")
X = int(input())
X += 8
print(f"X += 8 = {X}, Operator Penjumlahan")
print("-----------------------------")
X -= 8

print(f"X -= 8 = {X}, Operator Pengurangan")
print("-----------------------------")
X *= 8

print(f"X *= 8 = {X}, Operator Perkalian")
print("-----------------------------")
X /= 8

print(f"X /= 8 = {X}, Operator Pembagian")
print("-----------------------------")
X %= 8

print(f"X %= 8 = {X}, Operator Modulus")
print("-----------------------------")
X **= 8

print(f"X **= 8 = {X}, Operator Perpangkatan")
print("-----------------------------")


print("")
print("")
print("-----------------------------")
print("     Identity Operator")
print("-----------------------------")
angka1 = 10
angka2 = 10
angka3 = 5

print (angka1 is angka2)
print (id(angka1) is id(angka2))
print (angka1 is not angka3)
print (angka1 is angka3)




print("")
print("")
print("-----------------------------")
print("     Membership Operator")
print("-----------------------------")
angka = [1 , 2, 3, 4 ,5]

print ("1 in angka: ", 1 in angka)
print ("10 not in angka: ", 10 not in angka)