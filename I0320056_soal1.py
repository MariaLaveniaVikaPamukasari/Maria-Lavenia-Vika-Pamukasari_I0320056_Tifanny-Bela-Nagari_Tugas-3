#Mengisi list dengan 10 nama teman
list = ['Issa','Hafiz','Naufal','Harry','Ivan','Elsa','Rian','Ilham','Diva','Asyer']
print(list)
#Mengisi list indeks 4,6,7
print("list[4]:", list[4])
print("list[6:8]:", list[6:8])
#Mengubah nama teman di list 3,5,9
print("Nilai ada pada index 3:", list[3])
print("Nilai ada pada index 5:", list[5])
print("Nilai ada pada index 9:", list[9])
list[3] = 'Ojat'
list[5] = 'Alam'
list[9] = 'Maurich'
print("Nilai baru ada pada index 3:", list[3])
print("Nilai baru ada pada index 5:", list[5])
print("Nilai baru ada pada index 9:", list[9])
print("Mengubah nama teman pada indeks 3,5,9:", list)
#Menambahkan dua teman baru
list.extend(['Rara','Nana'])
print("Menambahkan dua teman baru:", list)
#Menampilkan semua teman dengan perulangan
print("Menampilkan semua nama teman dengan perulangan menggunakan for in:")
for nama_teman in list:
    print(nama_teman)
#Menampilkan panjang list
print("Panjang list:", len(list))


















