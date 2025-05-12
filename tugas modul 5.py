n=int(input("masukkan jumlah mahasiswa : "))
name=[]
nilai=[]
for i in range (1,n+1):
    nama=input("masukkan nama : ")
    pretest=int(input("masukkan nilai pretest : " ))
    postest=int(input("masukkan nilai postest : "))
    makalah=int(input("masukkan nilai makalah : "))
    total =round((pretest*0.4)+(postest*0.4)+(makalah*0.2), 2)
    name.append(nama)
    nilai.append(total)
print("-"*60)
print("|            Nama                                |  Nilai  |")
print("-"*60)
for i in range (n):
    print(f"|{name[i]:<20}                            |  {nilai[i]:5}  |")
print("-"*60)
total=0
for i in range (n):
    total=total+nilai[i]
    rr=round(total/n,3)
print("rata-rata",rr)
max_nilai = nilai[0]
min_nilai = nilai[0]
name_max = name[0]
name_min = name[0]
q=len(nilai)
for i in range(q):
    if nilai[i] > max_nilai:
        max_nilai = nilai[i]
        name_max = name[i]
    elif nilai[i] < min_nilai:
        min_nilai = nilai[i]
        name_min = name[i]
print("Nilai tertinggi:", max_nilai, name_max)
print("Nilai terendah: ", min_nilai, name_min)
drr=nilai[0]
nmdrr=name[0]
w=len(nilai)
for i in range (w):
    if nilai[i]>rr:
        drr=nilai[i]
        nmdrr=name[i]
        print("nilai diatas rata rata dan namanya : ",drr,nmdrr)