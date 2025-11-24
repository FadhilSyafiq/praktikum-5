a = []
print("Program Input Nilai")
print("="*19)

def buat_tabel() :
    print("Daftar Nilai")
    print("="*65)
    print("| NO |   NIM   |    NAMA    |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
    print("="*65)
    if a == [] :
        print("Data Kosong")
    else :
        for i, list in enumerate(a, start=1):
            print(f"{i}, {list["nim"]}, {list["nama"]}, {list["tugas"]},{list["uts"]},{list["uas"]},{list["tugas"]},{list["nilai_akhir"]:.02f}")
    print("="*65)

while True:
    menu = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:").lower()
    if menu == "l" :
        buat_tabel()
    elif menu == "t" :
        nim = input("NIM :")
        nama = input("Nama :")
        nilai_uts = int(input("Nilai UTS :"))
        nilai_uas = int(input("Nilai UAS :"))
        nilai_tugas = int(input("Nilai Tugas :"))
        nilai_akhir = (0.3 * nilai_tugas)+(0.35 * nilai_uts)+(0.35 * nilai_uas)
        data_entry = {
            "nim" : nim,
            "nama" : nama,
            "uts" : nilai_uts,
            "uas" : nilai_uas,
            "tugas" : nilai_tugas,
            "nilai_akhir" : nilai_akhir
         }
        a.append(data_entry)
    elif menu == "u" :
        nama = input("Cari nama :")
        if a == [] :
            print("Data Kosong")
        else :
            for i, list in enumerate(a, start=1):
                if list["nama"] == nama :
                    plihan_ubah = input("1. Mengubah NIM 2. Mengubah Nama 3. Mengubah Tugas 4. Mengubah Nilai UTS 5. Mengubah Nilai UAS")
                                                             
    #elif menu == "H"
    elif menu == "k" :
        break

    