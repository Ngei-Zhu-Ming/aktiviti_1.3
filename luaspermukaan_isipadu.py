#Atur cara untuk mengira jumlah luas permukaan dan isi padu sebuah tangki air berbentuk silinder
#Pengisytiharan pemboleh ubah dan pemalar
#input
jejari=float(input("Masukkan jejari tangki air:"))
tinggi=float(input("Masukkan tinggi tangki air:"))
pi=float(3.142)

#Proses
luas_permukaan_silinder=(pi*jejari*jejari*2)+(2*pi*jejari*tinggi)
isi_padu_silinder=pi*jejari*jejari*tinggi

#output
print("Luas permukaan silinder ialah",round(luas_permukaan_silinder,2))
print("Isi padu silinder ialah",round(isi_padu_silinder,2))
