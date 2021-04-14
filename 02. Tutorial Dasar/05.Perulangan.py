print("------------------------")
print("      For Loop")
print("------------------------")

for i in range(0, 10):
    print(i)

for n in range(10, 0, -1):
    print(n)

print("------------------------")
print("      While Loop")
print("------------------------")

i = 0
while i < 10:
	print (i)
	i += 1


print("------------------------")
print("     For Array Loop (List / Tuple / Dictionary)")
print("------------------------")

list_1 = [1, 2, 3, 4, 5]
tuple_1 = ('a', 'b', 'c', 'd', 'e')
dict_1 = {"nama":"Han Joon Hok", "kota":"Depok"}
string_1 = "lorem gundam kidul monday"

for elm in list_1:
    print(elm)

print("--------------------------")
print("Perulangan 2 List")
print("--------------------------")

nama = [ 'Andi','Angger','Randy']
divisi = ['Engineer','Dev','BA']

for x in range(len(nama)):
    print('divisi', nama[x], 'bagian di', divisi[x])



