nama=input("masukkan nama anda ")
umur=input("masukkan umur anda ")
jenis_kelamin=input("masukkan jenis kelamin ")
kode_maskapai=int(input("masukkan kode maskapai :"))
if kode_maskapai==3012:
    print("padang-jakarta")
elif kode_maskapai==4015:
    print("padang-batam")
elif kode_maskapai==4050:
    print("padang-bandung")
else :
    print("tujuan tidak ditemukan")
kelas=input("kelas apa=")
jumlah_tiket=int(input("berapa tiket yang anda inginkan? "))
if kode_maskapai == 3012 :
    if kelas == "ekonomi" :
        harga=800000
        if jumlah_tiket>=3 :
            diskon=800000*jumlah_tiket*20/100
    elif kelas == "bisnis" :
        harga=850000
        if jumlah_tiket>=3 :
            diskon=850000*jumlah_tiket*20/100
    elif kelas == "first class" :
        harga=900000
        if jumlah_tiket>=3 :
            diskon=900000*jumlah_tiket*20/100
elif kode_maskapai == 4015 :
    if kelas == "ekonomi" :
        harga=500000
        if jumlah_tiket>=3 :
            diskon=500000*jumlah_tiket*20/100
    elif kelas == "bisnis" :
        harga=550000
        if jumlah_tiket>=3 :
            diskon=550000*jumlah_tiket*20/100
    elif kelas == "first class" :
        harga=700000
        if jumlah_tiket>=3 :
            diskon=700000*jumlah_tiket*20/100
elif kode_maskapai == 4050 :
    if kelas == "ekonomi" :
        harga=700000
        if jumlah_tiket>=3 :
            diskon=700000*jumlah_tiket*20/100
    elif kelas == "bisnis" :
        harga=750000
        if jumlah_tiket>=3 :
            diskon=750000*jumlah_tiket*20/100
    elif kelas == "first class" :
         harga=850000
         if jumlah_tiket>=3 :
            diskon=850000*jumlah_tiket*20/100
else:
    print("kode tidak ditemukan")
if jumlah_tiket>3:
    total_harga=(harga*jumlah_tiket)-diskon 
    print("total harga = ",total_harga)
else:
    total_harga=(harga*jumlah_tiket)
    print("total harga = ",total_harga)


