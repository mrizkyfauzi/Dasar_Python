print("--------------------")
print("List Introduction")
print("--------------------")
a = [2, 4, 8, 10] #list berisi angka
b = ['a', 'b', 'c', 'd'] #list berisi karakter
c = ['bocah', 'pea', 'kekinian'] #list berisi string
d = [[1,2,3],[1,2,3],[1,2,3]] #list berisi list
e = [(1,2,3),(1,2,3),(1,2,3)] #list berisi tuple
f = [{'a':1,'b':2,'c':3},{'a':2,'b':3,'c':4},{'a':3,'b':4,'c':5}] #list berisi dictionary
g = [1, 'b', 2, 'loram', [1,2,3],(1,2,3), {'a':1,'b':2,'c':3}] #list campuran

print (a, ',List Berisi Angka')
print (b, ',List berisi Karakter')
print (c, ',List berisi Karakter')
print (d, ',list berisi list')
print (e, ',list berisi tuple')
print (f, ',list berisi dictionary')
print (d, ',list berisi campuran')

print("--------------------")
print("Accessing List")
print("--------------------")

a = [1, 2, 3, 4, 5]

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

for time in a:
    print(time)



print("-------------------")
print("  List Operation   ")
print("-------------------")

a = [1, 2, 3, 4, 5]

x = a + a
y = a * 10
z = list(map(lambda x: x + 1, a))
i = list(filter(lambda x: x % 2, a))

print(x)
print(y)
print(z)
print(i)

# Built-in function di python untuk operasi list
print("Ini yang ditambah")
jumlah = sum(a)
print(jumlah)

print("Ini yang terbesar")
terbesar = max(a)
print(terbesar)

print("Ini yang terkecil")
terkecil = min(a)
print(terkecil)

print("-------------------")
print("    List Method    ")
print("-------------------")

a = [3, 2, 1, 5, 4, 3, 3]
print(a)

#pengurutan dari belakang
a.reverse()
print(a)

a.sort()
print(a)

# Mengecek elemen yang mirip
print(a.count(3))

#Melihat isi list
print(a.index(4))
print(a.index(5))

#Mengubah isi list isi list
a.append(10)
print(a)

a.pop()
print(a)

a.insert(3, 20)
print(a)

a.remove(20)
print(a)

print("------------------")
print("Tuple Introduction")
print("------------------")

#list berisi angka
a = (1, 2, 3, 4, 5)

#list berisi karakter dan string
b = ('a','b','c','d')
c = ('lorem','ipsum','sit','dolor','amet')

#list berisi list, tuple, dictionary
d = ([1, 2, 3], [1, 2, 3], [1, 2, 3])
e = ((1, 2, 3), (1, 2, 3), (1, 2, 3))
f = ({'a':1, 'b':2, 'c':3}, {'a':2, 'b':3, 'c':4}, {'a':3, 'b':4, 'c':5})

#list campuran
g = (1, 'b', 2, 'lorem', [1,2,3], (1, 2, 3), {'a':1, 'b':2})

print (a)
print (b)
print (c)
print (d)
print (e)
print (f)
print (g)

print ("-----------------")
print ("Accessing Tuple")
print ("-----------------")

a = (1, 2, 3, 4, 5)

print (a[0])
print (a[1])
print (a[2])
print (a[3])
print (a[4])

for item in a:
    print(item)


print("---------------------")
print("Dictionary Introduction")
print("---------------------")

x = {
"foo":1,
"bar":999,
"lorem":{
    "ipsum":[20, 30, 40],
    "sit":"dolor",
    "amet":{
        "foo":1,
        "bar":2
    }
  }    
}

print(x)
print (type(x))

print(x['foo'])
print(x['bar'])
print(x['lorem'])
print(x['lorem']['ipsum'])
print(x['lorem']['amet'])
print(x['lorem']['amet']['foo'])

for key in x:
    print(key)

for key in x:
     print(x[key])