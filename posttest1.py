# data list utama
nimku = [2,0,0,9,1,0,6,0,5,3]

# sort ascending
def ascend(x) :
    for i in range(0,len(x)-1):
        for j in range(len(x)-1):
            if (x[j]>x[j+1]):
                temp = x[j]
                x[j]=x[j+1]
                x[j+1]=temp
                ascend(x)
    return x
x = nimku

# sort descending
def descend(c) :
    for i in range(0,len(c)-1):
        for j in range(len(c)-1):
            if (c[j]<c[j+1]):
                temp = c[j]
                c[j]=c[j+1]
                c[j+1]=temp
                descend(c)
    return c
c = nimku

# nilai max
def maksimal(bilangan):
    nilai_terbesar = bilangan[0]
    for nilai in bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar
a = nimku

# nilai min
def minimal(bilangan):
    nilai_terkecil = bilangan[0]
    for nilai in bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai
    return nilai_terkecil
a = nimku

# menambahkan data
def tambah() :
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
        "|               Menambahkan Data                |\n"
        "|_______________________________________________|\n"
        "|                                               |\n"
        "|     Menu Program   :                          |\n"
        "|     1. Menambahkan Satu Item(append())        |\n"
        "|     2. Menambahkan Beberapa Item(extends())   |\n"
        "|     3. Menyisipkan Item(insert())             |\n"
        "|     4. Kembali ke Menu                        |\n"
        "|_______________________________________________|\n")
    pilihan1 =int(input("Masukan Menu Pilihan(format angka) : "))
    if pilihan1 == 1 :
        nimku.append(int(input("Masukan Data yang Ingin Ditambah: ")))
        print("Hasilnya Adalah : \n",nimku)
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        tambah()
    elif pilihan1 == 2 :
        a = int(input("Berapa Banyak Data yang Ingin Ditambahkan?: "))
        for i in range(a):
            nimku.extend([int(input("Masukan Data yang Ingin Ditambah: "))])
        print("Hasilnya Adalah : \n",nimku)
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        tambah()
    elif pilihan1 == 3 :
        x = int(input("Indeks ke Berapa yang Ingin Disisipkan?: "))
        y = int(input("Masukan Data yang Ingin Disisipkan: "))
        nimku.insert(x,y)
        print(nimku)
        print("Hasilnya Adalah : \n",nimku)
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        tambah()
    elif pilihan1 == 4 :
        menu()
    else :
        print("Pilihan Tidak Tersedia\n")
        tambah()

# menghapus data
def hapus():
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
        "|                 Menghapus Data                |\n"
        "|_______________________________________________|\n"
        "|                                               |\n"
        "|     Menu Program   :                          |\n"
        "|     1. Metode del                             |\n"
        "|     2. Metode remove()                        |\n"
        "|     3. Metode pop()                           |\n"
        "|     4. Metode clear()                         |\n"
        "|     5. Kembali ke Menu                        |\n"
        "|_______________________________________________|\n")
    pilihan2 =int(input("Masukan Menu Pilihan(format angka) : "))
    if pilihan2 == 1 :
        mdel = int(input("Pilihlah salah satu metode del dibawah :\n"
        "1. Delete Satu Item\n"
        "2. Delete Beberapa Item\n"
        "3. Kembali\n"
        "Masukan Pilihan : "))
        if mdel == 1 :
            a = int(input("Indeks ke Berapa yang Dihapus?: "))
            del nimku[a]
            print("Hasilnya Adalah : \n",nimku)
        elif mdel == 2 :
            a = int(input("Dimulai dari Indeks ke Berapa Dihapus?: "))
            b = int(input("Sampai Indeks ke Berapa Dihapus?: "))
            del nimku[a:b]
            print("Hasilnya Adalah : \n",nimku)
        elif mdel == 3 :
            hapus()
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        hapus()

    elif pilihan2 == 2 :
        a = int(input("Masukan Elemen yang Akan Dihapus: "))
        nimku.remove(a)
        print("Hasilnya Adalah : \n",nimku)
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        hapus()
    elif pilihan2 == 3 :
        a = (int(input("Semua Indeks Dihapus, Pilih Satu Indeks untuk Disisakan: ")))
        print("Hasilnya Adalah : \n", nimku.pop(a))
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        hapus()
    elif pilihan2 == 4 :
        nimku.clear()
        print("Hasilnya Adalah : \n",nimku)
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        hapus()
    elif pilihan2 == 5 :
        menu()
    else :
        print("Pilihan Tidak Tersedia\n")
        hapus()

# mengupdate data
def update():
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
        "|                 Mengupdate Data               |\n"
        "|_______________________________________________|\n"
        "|                                               |\n"
        "|     Menu Program   :                          |\n"
        "|     1. Mengupdate Satu Elemen                 |\n"
        "|     2. Mengupdate Beberapa Elemen             |\n"
        "|     3. Kembali ke Menu                        |\n"
        "|_______________________________________________|\n")
    pilihan3 =int(input("Masukan Menu Pilihan(format angka) : "))
    if pilihan3 == 1 :
        a = int(input("\nMasukan Indeks ke Berapa yang Ingin Diupdate: "))
        b = int(input("\nMasukan Nilai Baru: "))
        nimku[a]=b
        print("Hasilnya Adalah : \n",nimku)
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        update()
    elif pilihan3 == 2 :
        a = int(input("\nDimulai dari Indeks ke Berapa Diupdate?: "))
        b = int(input("\nSampai Indeks ke Berapa Diupdate?: "))
        c = int(input("\nMasukan Nilai Baru: "))
        nimku[a : b]=[c]
        print("Hasilnya Adalah : \n",nimku)
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        update()
    elif pilihan3 == 3 :
        menu()
    else :
        print("Pilihan Tidak Tersedia\n")
        update()

# mengurutkan data
def urut() :
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
        "|                Mengurutkan Data               |\n"
        "|_______________________________________________|\n"
        "|                                               |\n"
        "|     Menu Program   :                          |\n"
        "|     1. Lanjutkan                              |\n"
        "|     2. Kembali ke Menu                        |\n"
        "|_______________________________________________|\n")
    pilihan4 =int(input("Masukan Menu Pilihan(format angka) : "))
    if pilihan4 == 1 :
        print("\nBerikut Urutan Secara Ascending\n\t",ascend(x))
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        urut()
    elif pilihan4 == 2 :
        menu()
    else :
        print("Pilihan Tidak Tersedia\n")
        urut()
# nilai terkecil dan terbesar
def minmax():
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
        "|                 Maks & Min Data               |\n"
        "|_______________________________________________|\n"
        "|                                               |\n"
        "|     Menu Program   :                          |\n"
        "|     1. Menampilkan Nilai Terbesar             |\n"
        "|     2. Menampilkan Nilai Terkecil             |\n"
        "|     3. Kembali ke Menu                        |\n"
        "|_______________________________________________|\n")
    pilihan5 =int(input("Masukan Menu Pilihan(format angka) : "))
    if pilihan5 == 1 :
        print("\nNilai Terbesar(Maks) adalah : ", maksimal(a))
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        minmax()
    if pilihan5 == 2 :
        print("\nNilai Terkecil(Min) adalah : ", minimal(a))
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        minmax()
    elif pilihan5 == 3 :
        menu()
    else :
        print("Pilihan Tidak Tersedia\n")
        minmax()

# menampilkan banyak data
def banyak():
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
        "|             Mengetahui Banyak Data            |\n"
        "|_______________________________________________|\n"
        "|                                               |\n"
        "|     Menu Program   :                          |\n"
        "|     1. Lanjutkan                              |\n"
        "|     2. Kembali ke Menu                        |\n"
        "|_______________________________________________|\n")
    pilihan6 =int(input("Masukan Menu Pilihan(format angka) : "))
    if pilihan6 == 1 :
        print("\nBanyak Data Dalam List Adalah : ", len(nimku))
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        banyak()
    elif pilihan6 == 2 :
        menu()
    else :
        print("Pilihan Tidak Tersedia\n")
        banyak()

# membalikan urutan data
def balik() :
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
        "|                Mengurutkan Data               |\n"
        "|_______________________________________________|\n"
        "|                                               |\n"
        "|     Menu Program   :                          |\n"
        "|     1. Lanjutkan                              |\n"
        "|     2. Kembali ke Menu                        |\n"
        "|_______________________________________________|\n")
    pilihan7 =int(input("Masukan Menu Pilihan(format angka) : "))
    if pilihan7 == 1 :
        print("\nBerikut Urutan Secara Descending\n\t",descend(c))
        input("\n>>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")
        balik()
    elif pilihan7 == 2 :
        menu()
    else :
        print("Pilihan Tidak Tersedia\n")
        balik()

def home() :
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
        "|                 Posttest 1 APL                |\n"
        "|_______________________________________________|\n"
        "|                                               |\n"
        "|     Nama : Duta Vira Pradhana Dipa            |\n"
        "|     NIM  : 2009106053                         |\n"
        "|     Kelas: Informatika B 20                   |\n"
        "|_______________________________________________|\n")
    input(">>>>>>>>>>>>>>>> Klilk Enter >>>>>>>>>>>>>>>>>>>")

def menu():
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
            "|                 Program List                  |\n"
            "|_______________________________________________|\n"
            "|                                               |\n"
            "|     Data List :                               |\n"
            "|\t"    ,nimku,                              "\t|\n"
            "|                                               |\n"
            "|     Menu Program   :                          |\n"
            "|     1. Menambahkan Data                       |\n"
            "|     2. Menghapus Data                         |\n"
            "|     3. Mengupdate Data                        |\n"
            "|     4. Mengurutkan Data                       |\n"
            "|     5. Mencari Nilai Min dan Max              |\n"
            "|     6. Menghitung Banyak Data dalam List      |\n"
            "|     7. Mengembailikan Urutan List             |\n"
            "|     8. Keluar                                 |\n"
            "|_______________________________________________|\n")
        pilihan =int(input("Masukan Menu Pilihan(format angka) : "))

        if pilihan == 1 :
            tambah()
        elif pilihan == 2 :
            hapus()
        elif pilihan == 3 :
            update()
        elif pilihan == 4 :
            urut()
        elif pilihan == 5 :
            minmax()
        elif pilihan == 6 :
            banyak()
        elif pilihan == 7 :
            balik()
        elif pilihan == 8 :
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|\n"
                "|                  Terimakasih                  |\n"
                "|_______________________________________________|\n")
            exit
        else :
            print("Pilihan Anda Tidak Tersedia\n")
            menu()
            
home()
menu()