# Import library
import os
import time
import pwinput

# Fungsi
# Fungsi delay
def delay(seconds):
    time.sleep(seconds)

# Fungsi 
def clear():
    os.system("cls")

# Fungsi Keluar
def quit(q):
    if q == "Y" or q == "y":
        clear()
        return True
    else:
        clear()
        return False

# Fungsi menu
# Menu utama
def menu():
    print("=" * 35)
    print("|" + "Pengubah Satuan Panjang".center(33) + "|")
    print("=" * 35)
    print("|".ljust(2) + "Pilih satuan yang ingin diubah:".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[1] Kilometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[2] Hektometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[3] Dekameter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[4] Meter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[5] Desimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[6] Centimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[7] Milimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[8] Keluar".ljust(31) + "|".rjust(2))
    print("=" * 35)

# Menu kilometer
def menu_kilometer():
    print("=" * 35)
    print("|" + "Kilometer".center(33) + "|")
    print("=" * 35)
    print("|".ljust(2) + "Ubah satuan kilometer ke:".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[1] Hektometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[2] Dekameter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[3] Meter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[4] Desimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[5] Centimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[6] Milimeter".ljust(31) + "|".rjust(2))
    print("=" * 35)

# Menu hektometer
def menu_hektometer():
    print("=" * 35)
    print("|" + "Hektometer".center(33) + "|")
    print("=" * 35)
    print("|".ljust(2) + "Ubah satuan hektometer ke:".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[1] Kilometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[2] Dekameter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[3] Meter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[4] Desimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[5] Centimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[6] Milimeter".ljust(31) + "|".rjust(2))
    print("=" * 35)

# Menu dekameter
def menu_dekameter():
    print("=" * 35)
    print("|" + "Dekameter".center(33) + "|")
    print("=" * 35)
    print("|".ljust(2) + "Ubah satuan dekameter ke:".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[1] Kilometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[2] Hektometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[3] Meter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[4] Desimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[5] Centimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[6] Milimeter".ljust(31) + "|".rjust(2))
    print("=" * 35)

# Menu meter
def menu_meter():
    print("=" * 35)
    print("|" + "Meter".center(33) + "|")
    print("=" * 35)
    print("|".ljust(2) + "Ubah satuan meter ke:".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[1] Kilometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[2] Hektometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[3] Dekameter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[4] Desimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[5] Centimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[6] Milimeter".ljust(31) + "|".rjust(2))
    print("=" * 35)

# Menu desimeter
def menu_desimeter():
    print("=" * 35)
    print("|" + "Desimeter".center(33) + "|")
    print("=" * 35)
    print("|".ljust(2) + "Ubah satuan desimeter ke:".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[1] Kilometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[2] Hektometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[3] Dekameter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[4] Meter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[5] Centimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[6] Milimeter".ljust(31) + "|".rjust(2))
    print("=" * 35)

# Menu centimeter
def menu_centimeter():
    print("=" * 35)
    print("|" + "Centimeter".center(33) + "|")
    print("=" * 35)
    print("|".ljust(2) + "Ubah satuan centimeter ke:".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[1] Kilometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[2] Hektometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[3] Dekameter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[4] Meter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[5] Desimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[6] Milimeter".ljust(31) + "|".rjust(2))
    print("=" * 35)

# Menu milimeter
def menu_milimeter():
    print("=" * 35)
    print("|" + "Milimeter".center(33) + "|")
    print("=" * 35)
    print("|".ljust(2) + "Ubah satuan milimeter ke:".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[1] Kilometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[2] Hektometer".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[3] Dekameter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[4] Meter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[5] Desimeter".ljust(31) + "|".rjust(2))
    print("|".ljust(2) + "[6] Centimeter".ljust(31) + "|".rjust(2))
    print("=" * 35)


# Class Kilometer
class Kilometer:
    def kmToHm(self, kilo):
        return kilo * 10
    def kmToDam(self, kilo):
        return kilo * (10 ** 2)
    def kmToM(self, kilo):
        return kilo * (10 ** 3)
    def kmToDm(self, kilo):
        return kilo * (10 ** 4)
    def kmToCm(self, kilo):
        return kilo * (10 ** 5)
    def kmToMm(self, kilo):
        return kilo * (10 ** 6)

# Class Hektometer
class Hektometer:
    def hmToKm(self, hekto):
        return hekto / 10
    def hmToDam(self, hekto):
        return hekto * 10
    def hmToM(self, hekto):
        return hekto * (10 ** 2)
    def hmToDm(self, hekto):
        return hekto * (10 ** 3)
    def hmToCm(self, hekto):
        return hekto * (10 ** 4)
    def hmToMm(self, hekto):
        return hekto * (10 ** 5)

# Class Dekameter
class Dekameter:
    def damToKm(self, deka):
        return deka / (10 ** 2)
    def damToHm(self, deka):
        return deka / 10
    def damToM(self, deka):
        return deka * 10
    def damToDm(self, deka):
        return deka * (10 ** 2)
    def damToCm(self, deka):
        return deka * (10 ** 3)
    def damToMm(self, deka):
        return deka * (10 ** 4)

# Class Meter
class Meter:
    def mToKm(self, meter):
        return meter / (10 ** 3)
    def mToHm(self, meter):
        return meter / (10 ** 2)
    def mToDam(self, meter):
        return meter / 10
    def mToDm(self, meter):
        return meter * 10
    def mToCm(self, meter):
        return meter * (10 ** 2)
    def mToMm(self, meter):
        return meter * (10 ** 3)

# Class Desimeter
class Desimeter:
    def dmToKm(self, desi):
        return desi / (10 ** 4)
    def dmToHm(self, desi):
        return desi / (10 ** 3)
    def dmToDam(self, desi):
        return desi / (10 ** 2)
    def dmToM(self, desi):
        return desi / 10
    def dmToCm(self, desi):
        return desi * 10
    def dmToMm(self, desi):
        return desi * (10 ** 2)

# Class Centimeter
class Centimeter:
    def cmToKm(self, desi):
        return desi / (10 ** 5)
    def cmToHm(self, desi):
        return desi / (10 ** 4)
    def cmToDam(self, desi):
        return desi / (10 ** 3)
    def cmToM(self, desi):
        return desi / (10 ** 2)
    def cmToDm(self, desi):
        return desi / 10
    def cmToMm(self, desi):
        return desi * 10

# Class Milimeter
class Milimeter:
    def mmToKm(self, mili):
        return mili / (10 ** 6)
    def mmToHm(self, mili):
        return mili / (10 ** 5)
    def mmToDam(self, mili):
        return mili / (10 ** 4)
    def mmToM(self, mili):
        return mili / (10 ** 3)
    def mmToDm(self, mili):
        return mili / (10 ** 2)
    def mmToCm(self, mili):
        return mili / 10

# Membuat objek
km = Kilometer()
hm = Hektometer()
dam = Dekameter()
m = Meter()
dm = Desimeter()
cm = Centimeter()
mm = Milimeter()

# Pilihan valid
banyakPilihan = tuple(i for i in range(9))
banyakPilihan2 = tuple(i for i in range(1, 7))

username = "iya" # iyhkidz
password = "enggak" # aphiyhbro77
salah = 0

# Looping program
while True:
    clear()
    print(f"\033[0mSisa percobaan login: {3 - salah}")
    usernameinput = input("Masukkan username: ")
    passwordinput = pwinput.pwinput(prompt="Masukkan password: ")

    if usernameinput == username and passwordinput == password:
        salah = 0
        print("Anda telah login")
        delay(1.5)
        clear()

        menu()

        try:
            pilihan = int(input("Masukkan pilihan anda: "))
            if pilihan in banyakPilihan:
                    try:
                        match pilihan:
                            # Kilometer
                            case 1:
                                delay(1)
                                clear()

                                try:
                                    kilo = float(input("Masukkan nilai dalam kilometer: "))
                                except ValueError:
                                    print("Masukkan nilai yang berupa angka.")

                                delay(1)
                                clear()

                                menu_kilometer()

                                try:
                                    pilihan2 = int(input("Masukkan pilihan anda: "))
                                except ValueError:
                                    print("Masukkan pilihan yang berupa angka")

                                if pilihan2 not in banyakPilihan2:
                                    print("Pilihan yang anda masukkan tidak ada di menu.")

                                delay(1)

                                try:
                                    match pilihan2:
                                        case 1:
                                            print(f"{kilo} Km sama dengan {km.kmToHm(kilo)} hm")
                                        case 2:
                                            print(f"{kilo} Km sama dengan {km.kmToDam(kilo)} dam")
                                        case 3:
                                            print(f"{kilo} Km sama dengan {km.kmToM(kilo)} m")
                                        case 4:
                                            print(f"{kilo} Km sama dengan {km.kmToDm(kilo)} dm")
                                        case 5:
                                            print(f"{kilo} Km sama dengan {km.kmToCm(kilo)} cm")
                                        case 6:
                                            print(f"{kilo} Km sama dengan {km.kmToMm(kilo)} mm")
                                except NameError:
                                    print("Input nilai yang anda masukkan tidak valid.")

                                if quit(input("Keluar? [Y/N]: ")):
                                    break
                            
                            # Hektometer
                            case 2:
                                delay(1)
                                clear()

                                try:
                                    hekto = float(input("Masukkan nilai dalam hektometer: "))
                                except ValueError:
                                    print("Masukkan nilai yang berupa angka.")

                                delay(1)
                                clear()

                                menu_hektometer()

                                try:
                                    pilihan2 = int(input("Masukkan pilihan anda: "))
                                except ValueError:
                                    print("Masukkan pilihan yang berupa angka")

                                if pilihan2 not in banyakPilihan2:
                                    print("Pilihan yang anda masukkan tidak ada di menu.")

                                delay(1)

                                try:
                                    match pilihan2:
                                        case 1:
                                            print(f"{hekto} hm sama dengan {hm.hmToKm(hekto)} Km")
                                        case 2:
                                            print(f"{hekto} hm sama dengan {hm.hmToDam(hekto)} dam")
                                        case 3:
                                            print(f"{hekto} hm sama dengan {hm.hmToM(hekto)} m")
                                        case 4:
                                            print(f"{hekto} hm sama dengan {hm.hmToDm(hekto)} dm")
                                        case 5:
                                            print(f"{hekto} hm sama dengan {hm.hmToCm(hekto)} cm")
                                        case 6:
                                            print(f"{hekto} hm sama dengan {hm.hmToMm(hekto)} mm")
                                except NameError:
                                    print("Input nilai yang anda masukkan tidak valid.")

                                if quit(input("Keluar? [Y/N]: ")):
                                    break

                            # Dekameter
                            case 3:
                                delay(1)
                                clear()

                                try:
                                    deka = float(input("Masukkan nilai dalam dekameter: "))
                                except ValueError:
                                    print("Masukkan nilai yang berupa angka.")

                                delay(1)
                                clear()

                                menu_dekameter()

                                try:
                                    pilihan2 = int(input("Masukkan pilihan anda: "))
                                except ValueError:
                                    print("Masukkan pilihan yang berupa angka")

                                if pilihan2 not in banyakPilihan2:
                                    print("Pilihan yang anda masukkan tidak ada di menu.")

                                delay(1)

                                try:
                                    match pilihan2:
                                        case 1:
                                            print(f"{deka} dam sama dengan {dam.damToKm(deka)} Km")
                                        case 2:
                                            print(f"{deka} dam sama dengan {dam.damToHm(deka)} hm")
                                        case 3:
                                            print(f"{deka} dam sama dengan {dam.damToM(deka)} m")
                                        case 4:
                                            print(f"{deka} dam sama dengan {dam.damToDm(deka)} dm")
                                        case 5:
                                            print(f"{deka} dam sama dengan {dam.damToCm(deka)} cm")
                                        case 6:
                                            print(f"{deka} dam sama dengan {dam.damToMm(deka)} mm")
                                except NameError:
                                    print("Input nilai yang anda masukkan tidak valid.")

                                if quit(input("Keluar? [Y/N]: ")):
                                    break

                            # Meter
                            case 4:
                                delay(1)
                                clear()

                                try:
                                    meter = float(input("Masukkan nilai dalam meter: "))
                                except ValueError:
                                    print("Masukkan nilai yang berupa angka.")

                                delay(1)
                                clear()

                                menu_meter()

                                try:
                                    pilihan2 = int(input("Masukkan pilihan anda: "))
                                except ValueError:
                                    print("Masukkan pilihan yang berupa angka")

                                if pilihan2 not in banyakPilihan2:
                                    print("Pilihan yang anda masukkan tidak ada di menu.")

                                delay(1)

                                try:
                                    match pilihan2:
                                        case 1:
                                            print(f"{meter} m sama dengan {m.mToKm(meter)} Km")
                                        case 2:
                                            print(f"{meter} m sama dengan {m.mToHm(meter)} hm")
                                        case 3:
                                            print(f"{meter} m sama dengan {m.mToDam(meter)} dam")
                                        case 4:
                                            print(f"{meter} m sama dengan {m.mToDm(meter)} dm")
                                        case 5:
                                            print(f"{meter} m sama dengan {m.mToCm(meter)} cm")
                                        case 6:
                                            print(f"{meter} m sama dengan {m.mToMm(meter)} mm")
                                except NameError:
                                    print("Input nilai yang anda masukkan tidak valid.")

                                # 
                                if quit(input("Keluar? [Y/N]: ")):
                                    break

                            # Desimeter
                            case 5:
                                delay(1)
                                clear()

                                try:
                                    desi = float(input("Masukkan nilai dalam desimeter: "))
                                except ValueError:
                                    print("Masukkan nilai yang berupa angka.")

                                delay(1)
                                clear()

                                menu_desimeter()

                                delay(1)

                                try:
                                    pilihan2 = int(input("Masukkan pilihan anda: "))
                                except ValueError:
                                    print("Masukkan pilihan yang berupa angka")

                                if pilihan2 not in banyakPilihan2:
                                    print("Pilihan yang anda masukkan tidak ada di menu.")

                                try:
                                    match pilihan2:
                                        case 1:
                                            print(f"{desi} dm sama dengan {dm.dmToKm(desi)} Km")
                                        case 2:
                                            print(f"{desi} dm sama dengan {dm.dmToHm(desi)} hm")
                                        case 3:
                                            print(f"{desi} dm sama dengan {dm.dmToDam(desi)} dam")
                                        case 4:
                                            print(f"{desi} dm sama dengan {dm.dmToM(desi)} m")
                                        case 5:
                                            print(f"{desi} dm sama dengan {dm.dmToCm(desi)} cm")
                                        case 6:
                                            print(f"{desi} dm sama dengan {dm.dmToMm(desi)} mm")
                                except NameError:
                                    print("Input nilai yang anda masukkan tidak valid.")

                                if quit(input("Keluar? [Y/N]: ")):
                                    break

                            # Centimeter
                            case 6:
                                delay(1)
                                clear()

                                try:
                                    centi = float(input("Masukkan nilai dalam centimeter: "))
                                except ValueError:
                                    print("Masukkan nilai yang berupa angka.")

                                delay(1)
                                clear()

                                menu_centimeter()

                                try:
                                    pilihan2 = int(input("Masukkan pilihan anda: "))
                                except ValueError:
                                    print("Masukkan pilihan yang berupa angka")

                                if pilihan2 not in banyakPilihan2:
                                    print("Pilihan yang anda masukkan tidak ada di menu.")

                                delay(1)

                                try:
                                    match pilihan2:
                                        case 1:
                                            print(f"{centi} cm sama dengan {cm.cmToKm(centi)} Km")
                                        case 2:
                                            print(f"{centi} cm sama dengan {cm.cmToHm(centi)} hm")
                                        case 3:
                                            print(f"{centi} cm sama dengan {cm.cmToDam(centi)} dam")
                                        case 4:
                                            print(f"{centi} cm sama dengan {cm.cmToM(centi)} m")
                                        case 5:
                                            print(f"{centi} cm sama dengan {cm.cmToDm(centi)} dm")
                                        case 6:
                                            print(f"{centi} cm sama dengan {cm.cmToMm(centi)} mm")
                                except NameError:
                                    print("Input nilai yang anda masukkan tidak valid.")

                                if quit(input("Keluar? [Y/N]: ")):
                                    break

                            # Milimeter
                            case 7:
                                delay(1)
                                clear()

                                try:
                                    mili = float(input("Masukkan nilai dalam milimeter: "))
                                except ValueError:
                                    print("Masukkan nilai yang berupa angka.")

                                delay(1)
                                clear()

                                menu_milimeter()

                                try:
                                    pilihan2 = int(input("Masukkan pilihan anda: "))
                                except ValueError:
                                    print("Masukkan pilihan yang berupa angka")

                                if pilihan2 not in banyakPilihan2:
                                    print("Pilihan yang anda masukkan tidak ada di menu.")

                                delay(1)

                                try:
                                    match pilihan2:
                                        case 1:
                                            print(f"{mili} mm sama dengan {mm.mmToKm(mili)} Km")
                                        case 2:
                                            print(f"{mili} mm sama dengan {mm.mmToHm(mili)} hm")
                                        case 3:
                                            print(f"{mili} mm sama dengan {mm.mmToDam(mili)} dam")
                                        case 4:
                                            print(f"{mili} mm sama dengan {mm.mmToM(mili)} m")
                                        case 5:
                                            print(f"{mili} mm sama dengan {mm.mmToDm(mili)} dm")
                                        case 6:
                                            print(f"{mili} mm sama dengan {mm.mmToCm(mili)} cm")
                                except NameError:
                                    print("Input nilai yang anda masukkan tidak valid.")

                                if quit(input("Keluar? [Y/N]: ")):
                                    break

                            case 8:
                                clear()
                                break
                    except NameError:
                        print("Input nilai yang anda masukkan tidak valid.")
        except ValueError:
            print("Masukkan pilihan yang berupa angka")


        else:
            delay(1.5)
            print("Pilihan yang anda masukkan tidak ada di menu.")


    else:
        salah += 1
        print("\033[1;31mUsername/Password salah")
        delay(0.5)
        if salah == 3:
            clear()
            print("\033[0mAnda sudah gagal 3 kali")
            break




