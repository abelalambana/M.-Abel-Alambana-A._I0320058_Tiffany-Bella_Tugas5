#Program harus dapat menerima input nama dan jenis kelamin pengguna program
name=(input('Masukkan Nama : '))
jk=(input('Jenis Kelamin (L/P) : ')).upper()

#Program menggunakan percabangan
if jk=='L':
	print('Selamat Datang, Tuan {}!'.format(name))
elif jk=='P':
	print('Selamat Datang, Nyonya {}!'.format(name))
else:
	pass
print()