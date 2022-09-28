# Default data
saya = {
    "Nama": "Muhammad Nabil Saragih",
    "Umur": 17,
    "NIM": "2209106032",
    "Jurusan": "Informatika",
    "Angkatan": "22"
}

while True:
    jalur = str(input("Tambah, Lihat, Ubah, atau Hapus? "))

    # Create
    if jalur == "Tambah" or jalur == "tambah":
        key = input("Masukkan key: ")
        value = input("Masukkan value: ")
        saya.update({key: value})

    # Read
    if jalur == "Lihat" or jalur == "lihat":
        print(saya)

    # Update
    if jalur == "Ubah" or jalur == "ubah":
        key = str(input("Masukkan key: "))
        value = input("Masukkan value baru: ")
        saya[key] = value

    # Delete
    if jalur == "Hapus" or jalur == "hapus":
        key = input("Masukkan nilai yang ingin dihapus: ")
        del saya[key]

    lanjut = input("Lanjutkan? [Ya/Tidak]: ")
    if lanjut == "Tidak" or lanjut == "tidak":
        break
