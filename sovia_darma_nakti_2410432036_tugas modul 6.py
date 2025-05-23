while True:
    barisA=int(input("masukkan baris matriks A"))
    kolomA=int(input("masukkan kolom matriks A"))
    barisB=int(input("masukkan baris matriks B"))
    kolomB=int(input("masukkan baris matriks B"))
    print("\nmasukkan matriks A")
    A=[]
    for i in range (barisA):
        A.append([])
        for j in range (kolomA):
            elemen=int(input(f"A[{i+1}][{j+1}]"))
            A[i].append(elemen)
    print("\ntampilan matriks A")
    for i in range (barisA):
        for j in range (kolomA):
            print(A[i][j],end=" ")
        print()
    print("\nmasukkan matriks B")
    B=[]
    for i in range (barisB):
        B.append([])
        for j in range (kolomB):
            elemen=int(input(f"B[{i+1}][{j+1}]"))
            B[i].append(elemen)
    print("\ntampilan matriks B")
    for i in range (barisB):
        for j in range (kolomB):
            print(B[i][j],end=" ")
        print()
    print("\nmenu kalkulator")
    print("\n=== MENU OPERASI MATRIKS ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Determinan")
    print("5. Invers")
    print("6. Transpose")
    print("0. Keluar")
    pilih = int(input("Pilih menu (0-6): "))
    if pilih==1:
        if barisA==barisB and kolomA==kolomB :
            print("\nhasil penjumlahan matriks A dan B")
            jumlah=[]
            for i in range (barisA):
                jumlah.append([])
                for j in range (kolomA):
                    hasil=A[i][j]+B[i][j]
                    jumlah[i].append(hasil)
            for i in range (len(jumlah)):
                for j in range (len(jumlah)):
                    print(jumlah[i][j],end="  ")
                print()
        else:
                print("matriks tidak sesuai")
    if pilih==2:
        if barisA==barisB and kolomA==kolomB :
            print("\nhasil pengurangan matriks A dan B")
            jumlah=[]
            for i in range (barisA):
                jumlah.append([])
                for j in range (kolomA):
                    hasil=A[i][j]-B[i][j]
                    jumlah[i].append(hasil)
            for i in range (len(jumlah)):
                for j in range (len(jumlah)):
                    print(jumlah[i][j],end="  ")
                print()
        else:
            print("matriks tidak sesuai")
    if pilih==3:
        if kolomA==barisB :
            print("\nhasil perkalian matriks A dan B")
            jumlah=[]
            for i in range (barisA):
                jumlah.append([])
                for j in range (kolomB):
                    total=0
                    for k in range (kolomA):
                        total+=A[i][k]*B[k][j]
                    jumlah[i].append(total)
            for i in range (len(jumlah)):
                for j in range (len(jumlah)):
                    print(jumlah[i][j],end="  ")
                print()
        else:
            print("matriks tidak sesuai")
    if pilih==4:
        if barisA==kolomA and barisB==kolomB:
            if barisA==kolomA:
                if barisA==2:
                    det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0] 
                    print("determinan matriks A=", det_A)
                elif barisA==3:
                    a=A
                    det_aa=(a[0][0]*a[1][1]*a[2][2] +
                            a[0][1]*a[1][2]*a[2][0] +
                            a[0][2]*a[1][0]*a[2][1] -
                            a[0][2]*a[1][1]*a[2][0] -
                            a[0][0]*a[1][2]*a[2][1] -
                            a[0][1]*a[1][0]*a[2][2])
                    print('determinan matriks A=',det_aa)
            if barisB==kolomB:
                if barisB==2:
                    det_b=B[0][0]*B[1][1] - B[0][1]*B[1][0]
                    print("determinan matriks B=", det_b)
                elif barisB==3:
                    b=B
                    det_bb=(b[0][0]*b[1][1]*b[2][2] +
                            b[0][1]*b[1][2]*b[2][0] +
                            b[0][2]*b[1][0]*b[2][1] -
                            b[0][2]*b[1][1]*b[2][0] -
                            b[0][0]*b[1][2]*b[2][1] -
                            b[0][1]*b[1][0]*b[2][2])
                    print("determinan matriks B=", det_bb)
        else:
            print("ukuran matriks tidak sesuai")
    if pilih == 5:
        if barisA == kolomA :
                n = barisA
                temp = []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        baris.append(A[i][j])
                    temp.append(baris)
                identitas = []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        if i == j:
                            baris.append(1.0)
                        else:
                            baris.append(0.0)
                    identitas.append(baris)
                for i in range(n):
                    if temp[i][i] == 0:
                        tukar = False
                        for k in range(i+1, n):
                            if temp[k][i] != 0:
                                t=temp[i]
                                temp[i]=temp[k]
                                temp[k]=t
                                t2=identitas[i]
                                identitas[i]=identitas[k]
                                identitas[k]=t2
                                break
                        if not tukar:
                            print("Matriks A tidak memiliki invers (determinan = 0)")
                            break
                    pembagi = temp[i][i]
                    for j in range(n):
                        temp[i][j] /= pembagi
                        identitas[i][j] /= pembagi
                    for k in range(n):
                        if k != i:
                            faktor = temp[k][i]
                            for j in range(n):
                                temp[k][j] -= faktor * temp[i][j]
                                identitas[k][j] -= faktor * identitas[i][j]
                else:
                    print("Invers Matriks A:")
                    for i in range(n):
                        print("[", end=" ")
                        for j in range(n):
                            print(f"{identitas[i][j]:^8.2f}", end=" ")
                        print("]")
        elif barisB == kolomB :
                n = barisB
                temp = []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        baris.append(B[i][j])
                    temp.append(baris)
                identitas = []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        if i == j:
                            baris.append(1.0)
                        else:
                            baris.append(0.0)
                    identitas.append(baris)
                for i in range(n):
                    if temp[i][i] == 0:
                        tukar = False
                        for k in range(i+1, n):
                             if temp[k][i] != 0:
                                t=temp[i]
                                temp[i]=temp[k]
                                temp[k]=t
                                t2=identitas[i]
                                identitas[i]=identitas[k]
                                identitas[k]=t2
                                break                                
                        if not tukar:
                            print("Matriks B tidak memiliki invers (determinan = 0)")
                            break
                    pembagi = temp[i][i]
                    for j in range(n):
                        temp[i][j] /= pembagi
                        identitas[i][j] /= pembagi

                    for k in range(n):
                        if k != i:
                            faktor = temp[k][i]
                            for j in range(n):
                                temp[k][j] -= faktor * temp[i][j]
                                identitas[k][j] -= faktor * identitas[i][j]
                else:
                    print("Invers Matriks B:")
                    for i in range(n):
                        print("[", end=" ")
                        for j in range(n):
                            print(f"{identitas[i][j]:^8.2f}", end=" ")
                        print("]")
        else:
            print("Matriks harus persegi dan berukuran 2x2 atau 3x3 untuk menghitung invers.")
    if pilih==6:
        print("\nMatriks transpos:")
    print("transpos matriks A")
    for j in range(kolomA):
        for i in range(barisA):
            print(A[i][j], end=" ")
        print()
    print("transpos matriks B")
    for j in range(kolomB):
        for i in range(barisB):
            print(B[i][j], end=" ")
        print() 

                