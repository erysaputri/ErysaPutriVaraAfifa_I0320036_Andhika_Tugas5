#memasukkan data
nama = input("Nama : ")
jenis_kelamin = input("Jenis kelamin (L/P) : ")

#Menyapa
if jenis_kelamin == 'L':
    print("Selamat datang, Tuan",nama,"!")
elif jenis_kelamin == 'P':
    print("Selamat datang, Nyonya",nama,"!")
else:
    pass