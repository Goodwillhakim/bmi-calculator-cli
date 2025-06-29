print("=" *41)
print("       Body Mass Index Calculator")
print("=" *41)

#Mengambil Data

Berat_Badan=float(input("Masukan Berat Badan Dalam Kg "))
Tinggi_Badan=float(input("Masukan Tinggi Badan Dalam Cm "))

#Penghitngan

Tinggi_M= Tinggi_Badan/100
Hasil= Berat_Badan / (Tinggi_M **2)
print(f"BMI Anda : {Hasil:.2f}")

#Mengolah Penghitungan

if Hasil < 18.5 :
    print("Kategori Kurus")
elif Hasil < 25 :
    print("Kategori Normal")
elif Hasil < 30 :
    print("Kelebihan Berat Badan")
else:
    print("Obesitas")    