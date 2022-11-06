# Import library
import os, time, pwinput
from prettytable import PrettyTable

# Membuat fungsi yang akan digunakan nanti
def clear():
    os.system("cls" if os.name == "nt" else os.system("clear"))

def delay(seconds):
    time.sleep(seconds)

# Setup tempat menyimpan data
dictAkun = {}
listAkun = []
akun = ""
dictFilm = {}
pilihan1 = tuple(i for i in range(1, 4))
pilihan2 = tuple(i for i in range(1, 6))

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
        if len(dictAkun) == 0:
            clear()
            print("Tidak ada akun. Anda harus membuat akun terlebih dahulu")
            userReg = input("Masukkan username yang anda inginkan... ")
            passReg = input("Masukkan password yang anda inginkan... ")
            accLevel = input("Register sebagai? [Admin/User]... ")
            dictAkun[userReg] = dict(password=passReg, accountLevel=accLevel.title())
        else:
            delay(1)
            clear()
            username = input("Masukkan username anda: ")
            password = pwinput.pwinput(prompt="Masukkan password anda: ")

            for i in dictAkun:
                listAkun.append(i)

            for i in listAkun:
                if i == username:
                    akun = i

            accNow = dictAkun.get(akun)
            if accNow.get("password") == password:
                print("Login successful")
                delay(1)
                while True:
                    if accNow.get("accountLevel") == "Admin":
                        clear()
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
                                dictFilm[judulFilm] = dict(TahunRilis=tahunFilm, Genre=genreFilm, Durasi=durasiFilm)
                            case 2:
                                clear()
                                if len(dictFilm) == 0:
                                    print("Film kosong, silakan input data film terlebih dahulu.")
                                else:
                                    table = PrettyTable(["Judul Film", "Tahun Rilis", "Genre Film", "Durasi Film"])
                                    for key, value in dictFilm.items():
                                        table.add_row([key, value.get("TahunRilis"), value.get("Genre"), value.get("Durasi")])
                                    table.align = "l"
                                    print(table)

                                lanjut = input("Lanjut? [Y/N]... ")
                                if lanjut == "N" or lanjut == "n":
                                    break
                            case 3:
                                clear()
                                judulFilmUbah = input("Masukkan judul film yang ingin diubah: ")
                                for film in dictFilm:
                                    if film == judulFilmUbah:
                                        print("Judul:", film, ":", dictFilm.get(film))
                                        ubah = input("Masukkan key dari value yang ingin diubah: ")
                                        jadi = input("Ubah menjadi: ")
                                        if ubah == "Judul" or ubah == "judul":
                                            dictFilm[str(jadi)] = dictFilm[str(film)]
                                            del dictFilm[str(film)]
                                            print("Film berhasil diubah")
                                        else:
                                            dictFilm[film][ubah] = jadi
                            case 4:
                                clear()
                                judulFilmHapus = input("Masukkan judul film yang ingin dihapus: ")
                                if judulFilmHapus in dictFilm:
                                    dictFilm.pop(judulFilmHapus)
                            case 5:
                                clear()
                                akun = ""
                                break

                    elif accNow.get("accountLevel") == "User":
                        clear()
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

                        if pilihan not in pilihan1:
                            print("Pilihan anda tidak ada di menu.")
                            delay(1)
                            continue

                        match pilihan:
                            case 1:
                                clear()
                                table = PrettyTable(["Judul Film", "Tahun Rilis", "Genre Film", "Durasi Film"])
                                for key, value in dictFilm.items():
                                    table.add_row([key, value.get("TahunRilis"), value.get("Genre"), value.get("Durasi")])
                                table.align = "l"
                                print(table)
                            case 2:
                                clear()
                                filmTitle = input("Masukkan judul film yang ingin anda cari: ")
                                if len(dictFilm) == 0:
                                    print("Data film masih kosong, tunggu admin mengisi data.")
                                else:
                                    for film in dictFilm:
                                        if film == filmTitle:
                                            print("Judul yang anda cari ditemukan.\n")
                                            searchTable = PrettyTable(["Judul Film", "Tahun Rilis", "Genre Film", "Durasi Film"])
                                            searchTable.add_row([film, dictFilm[film].get("TahunRilis"), dictFilm[film].get("Genre"), dictFilm[film].get("Durasi")])
                                            searchTable.align = "l"
                                            print(searchTable)
                                        else:
                                            print("Film yang anda cari tidak ditemukan")
                            case 3:
                                clear()
                                akun = ""
                                break

                        lanjut = input("Lanjut? [Y/N]... ")
                        if lanjut == "N" or lanjut == "n":
                            break
            else:
                print("Wrong password")
                delay(10)

    elif pilihan == 2:
        clear()
        userReg = input("Masukkan username yang anda inginkan... ")
        passReg = input("Masukkan password yang anda inginkan... ")
        accLevel = input("Register sebagai? [Admin/User]... ")
        dictAkun[userReg] = dict(password=passReg, accountLevel=accLevel.title())

    elif pilihan == 3:
        clear()
        break