dict = {'Nama':'Vicka', 'Hobi':['menari','menyayi','berenang'], 'Sosial media':['vickasarry_','vikasarry02','Vicka Sarry'], 'Lagu':['melukis senja','bertahan','mengejar mimpi'], 'Makanan':['klepon','ayam geprek','gado-gado']}
print("dict['Nama']:", dict['Nama'])
print("dict['Hobi']:", dict['Hobi'])
print("dict['Sosial media']:", dict['Sosial media'])
print("dict['Lagu']:", dict['Lagu'])
print("dict['Makanan']:", dict['Makanan'])


#Mengubah salah satu hobi dan sosial media
dict['Hobi'][1] = 'Membaca'
dict['Sosial media'][2] = '@Vickasarry'
print("dict['Hobi'[1]:", dict['Hobi'][1])
print("dict:", dict['Sosial media'][2])
#Menghapus dua makanan
del dict['Makanan'][:2]
print("dict['Makanan'][:2]:", dict['Makanan'][:2])
#Menambahkan satu hobi
dict['Hobi'] = 'Main gitar'
print("dict['Hobi']:", dict['Hobi'])