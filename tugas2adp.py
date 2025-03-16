
nama=input("masukkan nama anda :")
print(f"pemain {nama}")
print("#####SELAMAT BERMAIN#####")
n=int(input("pilih angka positif sampai berapa : "))
k=int(input("angka bom : "))
for n in range (1,n):
    m=n%k
    if m==0 :
        print( "bom", end=" ")
    else :
        print(n, end=" ")
print("==================================")
print("==================================")
print("==================================")
print("==================================")
print("==================================")
print("==================================")
print("==================================")
lawan=input("siapa namamu?")
print(f"pemain {lawan}")
tebak_angka=int(input(f"teba angka dari 1 - {n} :"))
if 1<=tebak_angka<=n :
   if tebak_angka%k==0 :
    print(tebak_angka," adalah bom,anda kalah")
   else:
    print(tebak_angka," anda menang")
elif tebak_angka>n :
   print("silahkan coba lagi")


