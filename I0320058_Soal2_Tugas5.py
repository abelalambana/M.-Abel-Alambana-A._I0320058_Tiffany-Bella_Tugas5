#Program harus dapat menerima input nama pengguna dan nilai yang berupa angka
nama=(input('Masukkan Namamu : '))
nilai=int(input('Masukkan Nilaimu : '))

surpris = 'Halo, '+ str(nama) +'! Nilai anda setelah dikonversikan adalah '

if nilai<60:
	print( surpris + 'E')
elif nilai < 65 and nilai >=60:
    print(surpris + 'C')
elif nilai < 70 and nilai >=65:
    print(surpris + 'C+')
elif nilai < 75 and nilai >=70:
    print(surpris + 'B')
elif nilai < 80 and nilai >=75:
    print(surpris + 'B+')
elif nilai < 85 and nilai >=80:
    print(surpris + 'A-')
elif nilai <= 100 and nilai >=85:
    print(surpris + 'A')
else:
    pass
print()