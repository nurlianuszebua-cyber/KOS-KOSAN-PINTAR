print("===================================")
print("       KOS-KOSAN PINTAR")
print(" Pengolah Data Penghuni dan Tagihan")
import json
import os
print("===================================")
print("Program berhasil dijalankan!")

# DATA PENGHUNI KOS

nama_penghuni = "Andi"
nomor_kamar = "A1"
nomor_hp = "081234567890"
harga_sewa = 500000
sudah_bayar = True

# MENAMPILKAN DATA

print("\nDATA PENGHUNI")
print("Nama Penghuni :", nama_penghuni)
print("Nomor Kamar   :", nomor_kamar)
print("Nomor HP      :", nomor_hp)
print("Harga Sewa    :", harga_sewa)
print("Sudah Bayar   :", sudah_bayar)

# CEK STATUS PEMBAYARAN

print("\nSTATUS PEMBAYARAN")

if sudah_bayar == True:
    print("Status: LUNAS")
else:
    print("Status: BELUM LUNAS")

# DATA BEBERAPA PENGHUNI KOS

daftar_nama = ["Andi", "Siti", "Budi", "Rina"]

print("\nDAFTAR PENGHUNI KOS")

for nama in daftar_nama:
    print("Nama Penghuni:", nama)

# DATA PENGHUNI MENGGUNAKAN LIST DAN DICTIONARY

# MEMBACA DATA PENGHUNI DARI FILE

if os.path.exists("data_kos.json"):
    with open("data_kos.json", "r") as file:
        daftar_penghuni = json.load(file)
else:
    daftar_penghuni = [
        {
            "nama": "Andi",
            "kamar": "A1",
            "harga": 500000,
            "status": "Lunas"
        },
        {
            "nama": "Siti",
            "kamar": "A2",
            "harga": 500000,
            "status": "Belum Lunas"
        },
        {
            "nama": "Budi",
            "kamar": "A3",
            "harga": 500000,
            "status": "Lunas"
        }
    ]

print("\nDATA SELURUH PENGHUNI")

for penghuni in daftar_penghuni:
    print("Nama:", penghuni["nama"])
    print("Kamar:", penghuni["kamar"])
    print("Harga:", penghuni["harga"])
    print("Status:", penghuni["status"])
    print("----------------------")

# FUNGSI MENGHITUNG TOTAL TAGIHAN

def hitung_total_tagihan(data_penghuni):
    total = 0

    for penghuni in data_penghuni:
        total = total + penghuni["harga"]

    return total


# MEMANGGIL FUNGSI

total_tagihan = hitung_total_tagihan(daftar_penghuni)

print("\nTOTAL TAGIHAN SELURUH PENGHUNI")
print("Total Tagihan: Rp", total_tagihan)

# FUNGSI RINGKASAN PEMBAYARAN

def tampilkan_ringkasan(data_penghuni):
    jumlah_lunas = 0
    jumlah_belum_lunas = 0
    total_tagihan = 0

    for penghuni in data_penghuni:
        total_tagihan += penghuni["harga"]

        if penghuni["status"] == "Lunas":
            jumlah_lunas += 1
        else:
            jumlah_belum_lunas += 1

    print("\n===== RINGKASAN DATA KOS =====")
    print("Jumlah penghuni       :", len(data_penghuni))
    print("Sudah membayar        :", jumlah_lunas)
    print("Belum membayar        :", jumlah_belum_lunas)
    print("Total seluruh tagihan : Rp", total_tagihan)


# INPUT DATA PENGHUNI BARU

# MENU UTAMA PROGRAM

while True:
    print("\n===== KOS-KOSAN PINTAR =====")
    print("1. Lihat daftar penghuni")
    print("2. Tambah penghuni")
    print("3. Lihat ringkasan tagihan")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        print("\nDAFTAR PENGHUNI")
        for penghuni in daftar_penghuni:
            print("Nama:", penghuni["nama"])
            print("Kamar:", penghuni["kamar"])
            print("Harga: Rp", penghuni["harga"])
            print("Status:", penghuni["status"])
            print("-------------------")

    elif pilihan == "2":
        print("\nTAMBAH PENGHUNI")

        nama_baru = input("Nama penghuni: ")
        kamar_baru = input("Nomor kamar: ")
        harga_baru = int(input("Harga sewa: "))
        status_baru = input("Status (Lunas/Belum Lunas): ")

        penghuni_baru = {
            "nama": nama_baru,
            "kamar": kamar_baru,
            "harga": harga_baru,
            "status": status_baru
        }

        daftar_penghuni.append(penghuni_baru)

        with open("data_kos.json", "w") as file:
            json.dump(daftar_penghuni, file, indent=4)

        print("Data penghuni berhasil ditambahkan!")
        print("Data berhasil disimpan!")

    elif pilihan == "3":
        tampilkan_ringkasan(daftar_penghuni)

    elif pilihan == "4":
        print("Terima kasih telah menggunakan program!")
        break

    else:
        print("Pilihan tidak tersedia. Silakan coba lagi.")