"""
Dasar sintaksis dengan tipe data list
"""
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
print('Tampilkan variabel daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[3])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Denias', 312, -3.14]
print('\nTampilkan dengan for in range dengan data berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
print('Tambahkan 1 buku baru')
daftar_buku.append('Dunia matematika kelas 4')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTambahkan buku IPS')
daftar_buku.append('IPS kelas 4')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTambahkan 1 buku lagi')
daftar_buku.append('RPUL')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nHilangkan Macbeth dari daftar')
daftar_buku.remove('Macbeth')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
daftar_buku[0] = 'Denias'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen kedua')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
del daftar_buku[0:-3] #start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del step')
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
del daftar_buku[1::2] #start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')

print('\nMembuat list baru')
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan comprehension, ganjil')
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension, genap')
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension, hanya diujung')
daftar_buku = ['Macbeth', 'Moby Dick', 'Ramayana', 'Three Musketeers']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])



