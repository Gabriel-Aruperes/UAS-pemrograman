buku = []
buku_dipinjam = []

print("Perpustakaan Digital")

while True:
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Cari Buku")
    print("4. Tampilkan Buku")
    print("5. Pinjam Buku")
    print("6. Kembalikan Buku")
    print("7. Daftar Buku Dipinjam")
    print("8. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        judul = input("Judul: ")
        penulis = input("Penulis: ")
        tahun_terbit = input("Tahun Terbit: ")
        buku.append({"judul": judul, "penulis": penulis, "tahun_terbit": tahun_terbit})
        print("Buku berhasil ditambahkan.")

    elif pilihan == "2":
        judul = input("Judul buku untuk dihapus: ")
        for i, buku_item in enumerate(buku):
            if buku_item["judul"] == judul:
                konfirmasi = input("Apakah Anda yakin? (y/n): ")
                if konfirmasi.lower() == 'y':
                    del buku[i]
                    print("Buku berhasil dihapus.")
                    break

    elif pilihan == "3":
        kata_kunci = input("Kata kunci: ")
        hasil = [buku_item for buku_item in buku if kata_kunci.lower() in buku_item["judul"].lower()]
        for buku_item in hasil:
            print(f"Judul: {buku_item['judul']}, Penulis: {buku_item['penulis']}, Tahun Terbit: {buku_item['tahun_terbit']}")

    elif pilihan == "4":
        for i, buku_item in enumerate(buku):
            print(f"{i+1}. Judul: {buku_item['judul']}, Penulis: {buku_item['penulis']}, Tahun Terbit: {buku_item['tahun_terbit']}")

    elif pilihan == "5":
        judul = input("Judul buku untuk dipinjam: ")
        for buku_item in buku:
            if buku_item["judul"] == judul:
                buku_dipinjam.append(buku_item)
                buku.remove(buku_item)
                print("Buku berhasil dipinjam.")
                break
        else:
            print("Buku tidak tersedia.")

    elif pilihan == "6":
        judul = input("Judul buku untuk dikembalikan: ")
        for i, buku_item in enumerate(buku_dipinjam):
            if buku_item["judul"] == judul:
                buku.append(buku_item)
                del buku_dipinjam[i]
                print("Buku berhasil dikembalikan.")
                break
        else:
            print("Buku tidak ditemukan.")

    elif pilihan == "7":
        print("Daftar Buku Dipinjam:")
        for i, buku_item in enumerate(buku_dipinjam):
            print(f"{i+1}. Judul: {buku_item['judul']}, Penulis: {buku_item['penulis']}, Tahun Terbit: {buku_item['tahun_terbit']}")

    elif pilihan == "8":
        break
    else:
        print("Pilihan tidak valid.")
