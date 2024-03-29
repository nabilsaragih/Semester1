# Import library
import os, time, pwinput

# Membuat fungsi yang akan digunakan nanti
def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def delay(seconds):
    time.sleep(seconds)

# Setup tempat menyimpan data
listAkun = [[], [], []]
indexAkun = 0
listFilm = []
indexFilm = 0
pilihan1 = tuple(i for i in range(1, 4))
pilihan2 = tuple(i for i in range(1, 6))
pilihan3 = tuple(i for i in range(1, 4))

while True:
    clear()
    print("-" * 26)
    print("|", "Welcome to CRUD21".center(22), "|")
    print("-" * 26)
    print("|", "[1]", "Login".ljust(18),  "|")
    print("|", "[2]", "Register".ljust(18),  "|")
    print("|", "[3]", "Keluar".ljust(18),  "|")
    print("-" * 26)

    try:
        pilihan = int(input("Masukkan pilihan anda: "))
    except ValueError:
        print("Nilai yang anda masukkan haruslah angka.")

    if pilihan not in pilihan1:
        print("Pilihan anda tidak ada di menu.")
        delay(1)
        continue

    if pilihan == 1:
        if len(listAkun[0]) == 0:
            clear()
            print("Tidak ada akun. Anda harus membuat akun terlebih dahulu")
            userReg = input("Masukkan username yang anda inginkan... ")
            passReg = input("Masukkan password yang anda inginkan... ")
            accLevel = input("Register sebagai? [Admin/User]... ")

            listAkun[0].append(userReg)
            listAkun[1].append(passReg)
            listAkun[2].append(accLevel)

        else:
            delay(1)
            clear()
            username = input("Masukkan username anda: ")
            password = pwinput.pwinput(prompt="Masukkan password anda: ")

            for user in range(len(listAkun[0])):
                if listAkun[0][user] == username:
                    indexAkun += user

            if listAkun[1][indexAkun] == password:
                delay(1)
                print("Login successful")
                while True:
                    delay(1)
                    clear()
                    if listAkun[2][indexAkun] == "Admin" or listAkun[2][indexAkun] == "admin":
                        print("-" * 26)
                        print("|", "CRUD21 Admin Menu".center(22), "|")
                        print("-" * 26)
                        print("|", "[1]", "Tambah Film".ljust(18),  "|")
                        print("|", "[2]", "Lihat Film".ljust(18),  "|")
                        print("|", "[3]", "Ubah Film".ljust(18),  "|")
                        print("|", "[4]", "Hapus Film".ljust(18),  "|")
                        print("|", "[5]", "Logout".ljust(18),  "|")
                        print("-" * 26)

                        try:
                            pilihan = int(input("Masukkan pilihan anda: "))
                        except ValueError:
                            print("Nilai yang anda masukkan haruslah angka.")

                        if pilihan not in pilihan2:
                            print("Pilihan anda tidak ada di menu.")
                            delay(1)
                            continue

                        match pilihan:
                            case 1:
                                clear()
                                judulFilm = input("Masukkan judul film: ")
                                tahunFilm = input("Masukkan tahun rilis film: ")
                                genreFilm = input("Masukkan genre film: ")
                                durasiFilm = input("Masukkan durasi film: ")
                                listFilm.append(dict(Judul=judulFilm, TahunRilis=tahunFilm, Genre=genreFilm, Durasi=durasiFilm))

                            case 2:
                                clear()
                                if len(listFilm) == 0:
                                    print("Film kosong, silakan input data film terlebih dahulu.")
                                else:
                                    for i in range(1, len(listFilm) + 1):
                                        print(f"{i}. Judul: {listFilm[indexFilm]['Judul']}\n   Tahun Rilis: {listFilm[indexFilm]['TahunRilis']}\n   Genre: {listFilm[indexFilm]['Genre']}\n   Durasi: {listFilm[indexFilm]['Durasi']}\n")
                                        indexFilm += 1
                                    indexFilm = 0

                                lanjut = input("Lanjut? [Y/N]... ")
                                if lanjut == "N" or lanjut == "n":
                                    break

                            case 3:
                                clear()
                                judulFilmUbah = input("Masukkan judul film yang ingin diubah: ")
                                for film in listFilm:
                                    if film["Judul"] == judulFilmUbah:
                                        print(film)
                                        key = input("Masukkan key dari film yang ingin diubah: ")
                                        value = input("Ubah menjadi: ")
                                        film[key] = value

                            case 4:
                                clear()
                                judulFilmHapus = input("Masukkan judul film yang ingin dihapus: ")
                                for film in range(len(listFilm)):
                                    if listFilm[film]["Judul"] == judulFilmHapus:
                                        indexFilm += film
                                del listFilm[indexFilm]
                                indexFilm = 0

                            case 5:
                                clear()
                                indexAkun = 0
                                break

                    elif listAkun[2][indexAkun] == "User" or listAkun[2][indexAkun] == "user":
                        print("-" * 26)
                        print("|", "CRUD21 User Menu".center(22), "|")
                        print("-" * 26)
                        print("|", "[1]", "Lihat List Film".ljust(18),  "|")
                        print("|", "[2]", "Cari Film".ljust(18),  "|")
                        print("|", "[3]", "Logout".ljust(18),  "|")
                        print("-" * 26)

                        try:
                            pilihan = int(input("Masukkan pilihan anda: "))
                        except ValueError:
                            print("Nilai yang anda masukkan haruslah angka.")

                        if pilihan not in pilihan3:
                            print("Pilihan anda tidak ada di menu.")
                            delay(1)
                            continue

                        match pilihan:
                            case 1:
                                clear()
                                for i in range(1, len(listFilm) + 1):
                                    print(f"{i}. Judul: {listFilm[indexFilm]['Judul']}\n   Tahun Rilis: {listFilm[indexFilm]['TahunRilis']}\n   Genre: {listFilm[indexFilm]['Genre']}\n   Durasi: {listFilm[indexFilm]['Durasi']}\n")
                                    indexFilm += 1
                                indexFilm = 0

                            case 2:
                                clear()
                                filmTitle = input("Masukkan judul film yang ingin anda cari: ")
                                if len(listFilm) == 0:
                                    print("Data film masih kosong, tunggu admin mengisi data.")
                                else:
                                    for film in listFilm:
                                        if film["Judul"] == filmTitle:
                                            print("Judul yang anda cari ditemukan.\n")
                                            print(f"Judul Film: {film['Judul']}")
                                            print(f"Tahun Rilis: {film['TahunRilis']}")
                                            print(f"Genre Film: {film['Genre']}")
                                            print(f"Durasi Film: {film['Durasi']}\n")
                                        else:
                                            print("Film yang anda cari tidak ditemukan")

                                lanjut = input("Lanjut? [Y/N]... ")
                                if lanjut == "N" or lanjut == "n":
                                    break

                            case 3:
                                break

            else:
                print("Wrong password")
                indexAkun = 0

    elif pilihan == 2:
        userReg = input("Masukkan username yang anda inginkan... ")
        passReg = input("Masukkan password yang anda inginkan... ")
        accLevel = input("Register sebagai? [Admin/User]... ")

        listAkun[0].append(userReg)
        listAkun[1].append(passReg)
        listAkun[2].append(accLevel)

    elif pilihan == 3:
        clear()
        break