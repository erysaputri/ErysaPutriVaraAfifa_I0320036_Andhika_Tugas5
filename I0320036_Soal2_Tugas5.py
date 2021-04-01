#memasukkan data
nama = input("Nama : ")
nilai_angka = int(input("Nilai : "))
output = "Halo, " + nama + "!" + " Nilai Anda setelah dikonversi adalah"

#konversi nilai
if 85 <= nilai_angka <= 100:
    print(output,'A')
elif 80 <= nilai_angka <= 84:
    print(output,'A-')
elif 75 <= nilai_angka <= 79:
    print(output,'B+')
elif 70 <= nilai_angka <= 74:
    print(output,'B')
elif 65 <= nilai_angka <= 69:
    print(output,'C+')
elif 60 <= nilai_angka <= 64:
    print(output,'C')
elif 60 > nilai_angka:
    print(output,'E')
else:
    pass