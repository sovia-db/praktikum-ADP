def data_mahasiswa():
    data=[]
    jumlah=int(input("masukkan jumlah mahasiswa : "))
    for i in range (jumlah):
        print(f"\ndata mahasiswa ke {i+1}: ")
        nama=input("NAMA = ")
        nim=int(input("NIM : "))
        uts=float(input("UTS : "))
        uas=float(input("UAS : "))
        tugas=float(input("NILAI TUGAS : "))
        mahasiswa = [nama, nim, uts, uas, tugas, 0, 0]
        data.append(mahasiswa)
    return(data)
def hit_nilai_akhir(data):
    for m in data:
        m[5]=round(0.35*m[2]+0.35*m[3]+0.3*m[4],2)
def hit_rata(data,index):
    total=0
    for m in data:
        total+=m[index]
    return round(total/len(data),2)
def peringkat(data):
    for i in range(len(data)):
         rank=1
         for j in range (len(data)):
             if data[j][5]>data[i][5]:
                 rank+=1
         data[i][6]=rank
def tabel(data):
     print("\n{:<10} {:<10} {:<10} {:<10} {:<10} {:<13} {:<13}".format(
        "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir  ", "Peringkat"
    ))
     print("-"*75)
     for m in data:
          print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<13} {:<13}".format(
            m[0], m[1], m[2], m[3],
            m[4], m[5], m[6]
        ))
     print("-"*75)
     print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<13} {:<13}".format(
        "", "", 
     hit_rata(data, 2),
     hit_rata(data, 3),
     hit_rata(data, 4),
     hit_rata(data, 5),
        ""
    ))
def urutkan_nilai_akhir_tinggi(data):
    data_asli = []
    for m in data:
        data_asli.append(m)
    data_urut = []
    while len(data_asli) > 0:
        maks = data_asli[0]
        for m in data_asli:
            if m[5] > maks[5]:
                maks = m
        data_urut.append(maks)
        data_asli.remove(maks)
    return data_urut
data = data_mahasiswa()
hit_nilai_akhir(data)
peringkat(data)
data_urut = urutkan_nilai_akhir_tinggi(data)
tabel(data_urut)
