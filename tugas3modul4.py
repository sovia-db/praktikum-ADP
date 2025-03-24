while True:
    r = int(input("Masukkan jumlah baris kursi (minimal 4): "))
    c = int(input("Masukkan jumlah kolom kursi (minimal 4): "))
    if c < 4 or r < 4:
        print("Masukkan baris dan kolom kembali! Ukuran minimal bioskop adalah 4x4.")
        continue
    break
print("\nLayout Kursi Bioskop:")
for i in range (r):
    for j in range (c):
      print(i*c+j+1,end="\t")
    print()
kursi_terisi=""
while True :
   kursi_dipilih=1
   input_kursi=int(input("\npilihlah kursi anda (0 untk selesai): "))
   if input_kursi==0 :
      print("Terima kasih telah memesan tiket!")
      break
   input_dipilih=str(input_kursi)
   if f"{input_dipilih}" in f"{kursi_terisi}" :
         print(f"kursi {input_kursi} sudah di pesan,silahkan pesan lagi")
   elif 1<=input_kursi<=r*c :
            print(f"kursi {input_kursi} berhasil dipesan ")
   else:
       print(f"kursi {input_kursi} tidak valid, silahkan coba lagi")
   kursi_terisi+= input_dipilih +""
   print("\nLayout Kursi Bioskop terbaru:")
   for i in range (r):
      print()
      for j in range (c):
         if str(kursi_dipilih) in kursi_terisi:
               print("X",end="\t")
         else :
               print(f"{kursi_dipilih}",end="\t")
         kursi_dipilih+=1
   print()