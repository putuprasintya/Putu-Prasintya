barang_toko = [
    {"ID": "001", "Nama": "Deterjen Bubuk", "Harga": 50000, "Stok": 100, "Kategori": "Deterjen", "Supplier": "PT. Kebersihan Prima"},
    {"ID": "002", "Nama": "Deterjen Cair", "Harga": 60000, "Stok": 80, "Kategori": "Deterjen", "Supplier": "CV. Deterjen Sehat"},
    {"ID": "003", "Nama": "Pewangi Pakaian", "Harga": 25000, "Stok": 150, "Kategori": "Pewangi", "Supplier": "PT. Kebersihan Prima"},
    {"ID": "004", "Nama": "Pelembut Pakaian", "Harga": 30000, "Stok": 120, "Kategori": "Pelembut", "Supplier": "CV. Laundry Sejahtera"},
    {"ID": "005", "Nama": "Pemutih Pakaian", "Harga": 35000, "Stok": 70, "Kategori": "Pemutih", "Supplier": "PT. Pemutih Bersih"},
    {"ID": "006", "Nama": "Penghilang Noda", "Harga": 40000, "Stok": 60, "Kategori": "Penghilang Noda", "Supplier": "CV. Deterjen Sehat"},
    {"ID": "007", "Nama": "Pewangi Semprot Pakaian", "Harga": 30000, "Stok": 50, "Kategori": "Pewangi", "Supplier": "PT. Kebersihan Prima"},
    {"ID": "008", "Nama": "Deterjen Matic", "Harga": 55000, "Stok": 90, "Kategori": "Deterjen", "Supplier": "PT. Deterjen Maju"},
    {"ID": "009", "Nama": "Karbol Penghilang Bau", "Harga": 20000, "Stok": 110, "Kategori": "Penghilang Bau", "Supplier": "CV. Deterjen Sehat"},
    {"ID": "010", "Nama": "Pengering Pakaian Portable", "Harga": 150000, "Stok": 30, "Kategori": "Alat Laundry", "Supplier": "PT. Laundry Teknologi"}
]

# Fungsi untuk memvalidasi ID unik
def cek_id_unik(id_barang):
    for barang in barang_toko:
        if barang['ID'] == id_barang:
            return False
    return True

# Fungsi Pencarian Barang
def cari_barang(query):
    return [barang for barang in barang_toko if query == barang['ID'].lower() or
                                              query in barang['Nama'].lower() or
                                              query in barang['Kategori'].lower() or
                                              query in barang['Supplier'].lower()]

# Fungsi untuk menampilkan detail barang
def tampilkan_data_barang(barang):
    print(f"ID: {barang['ID']}, Nama: {barang['Nama']}, Harga: Rp{barang['Harga']:.0f}, Stok: {barang['Stok']}, Kategori: {barang['Kategori']}, Supplier: {barang['Supplier']}")

# Fungsi Validasi Angka
def input_angka(prompt, tipe=int, minimum=None):
    while True:
        try:
            angka = tipe(input(prompt))
            if minimum is not None and angka < minimum:
                print(f"Input harus lebih dari {minimum}.")
            else:
                return angka
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang benar.")

# Fungsi Konfirmasi
def konfirmasi_aksi(prompt):
    while True:
        pilihan = input(prompt).lower()
        if pilihan in ['ya', 'tidak']:
            return pilihan == 'ya'
        else:
            print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")

# Fungsi Create - Menambahkan data barang baru dengan validasi ID unik dan harga/stok positif
def tambah_barang():
    while True:
        id_barang = input("Masukkan ID Barang: ")
        if cek_id_unik(id_barang):
            break
        else:
            print("ID sudah digunakan. Masukkan ID lain.")

    nama_barang = input("Masukkan Nama Barang: ")
    harga_barang = input_angka("Masukkan Harga Barang: ", float, 0)
    stok_barang = input_angka("Masukkan Jumlah Stok: ", int, 0)
    kategori_barang = input("Masukkan Kategori Barang: ")
    supplier_barang = input("Masukkan Supplier Barang: ")

    barang = {
        "ID": id_barang,
        "Nama": nama_barang,
        "Harga": harga_barang,
        "Stok": stok_barang,
        "Kategori": kategori_barang,
        "Supplier": supplier_barang
    }

    barang_toko.append(barang)
    print("Barang berhasil ditambahkan!\n")

# Fungsi Read - Menampilkan seluruh data barang
def tampilkan_barang():
    if not barang_toko:
        print("Tidak ada barang yang tersedia.\n")
        return

    print("\nData Barang Toko:")
    for barang in barang_toko:
        tampilkan_data_barang(barang)
    print("")

# Fungsi Update - Mengubah data barang setelah menampilkan data lengkap
def ubah_barang():
    query = input("Masukkan ID/Nama/Kategori/Supplier barang yang akan diubah: ").lower()
    hasil_pencarian = cari_barang(query)

    if not hasil_pencarian:
        print("Barang tidak ditemukan berdasarkan pencarian tersebut.\n")
        return

    if len(hasil_pencarian) == 1:
        barang = hasil_pencarian[0]
        tampilkan_data_barang(barang)
    else:
        print(f"{len(hasil_pencarian)} barang ditemukan:")
        for idx, barang in enumerate(hasil_pencarian):
            print(f"{idx+1}. ", end="")
            tampilkan_data_barang(barang)

        pilihan_ubah = input_angka("Masukkan nomor barang yang ingin diubah: ", int, 1)
        barang = hasil_pencarian[pilihan_ubah - 1]
        tampilkan_data_barang(barang)

    # Menu ubah data barang
    while True:
        print("\nPilih data yang ingin diubah:")
        print("1. Nama Barang")
        print("2. Harga Barang")
        print("3. Jumlah Stok")
        print("4. Kategori Barang")
        print("5. Supplier Barang")
        print("6. Tampilkan Data Terbaru")
        print("7. Kembali")

        pilihan = input("Masukkan pilihan (1-7): ")

        if pilihan == "1":
            barang['Nama'] = input("Masukkan Nama Barang baru: ")
            print("Nama barang berhasil diubah!")
        elif pilihan == "2":
            barang['Harga'] = input_angka("Masukkan Harga Barang baru: ", float, 0)
            print("Harga barang berhasil diubah!")
        elif pilihan == "3":
            barang['Stok'] = input_angka("Masukkan Jumlah Stok baru: ", int, 0)
            print("Stok barang berhasil diubah!")
        elif pilihan == "4":
            barang['Kategori'] = input("Masukkan Kategori Barang baru: ")
            print("Kategori barang berhasil diubah!")
        elif pilihan == "5":
            barang['Supplier'] = input("Masukkan Supplier Barang baru: ")
            print("Supplier barang berhasil diubah!")
        elif pilihan == "6":
            print("\nData barang terbaru setelah perubahan:")
            tampilkan_data_barang(barang)
        elif pilihan == "7":
            print("Kembali ke menu sebelumnya.\n")
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi Restock dan Penjualan Barang dengan Parameter
def ubah_stok_barang(query, tipe_aksi):
    hasil_pencarian = cari_barang(query)

    if not hasil_pencarian:
        print("Barang tidak ditemukan berdasarkan pencarian tersebut.\n")
        return

    if len(hasil_pencarian) == 1:
        barang = hasil_pencarian[0]
        tampilkan_data_barang(barang)
        jumlah_stok = input_angka(f"Masukkan jumlah stok {'tambahan' if tipe_aksi == 'restock' else 'terjual'}: ", int, 1)
        if tipe_aksi == 'restock':
            barang['Stok'] += jumlah_stok
        else:
            if jumlah_stok > barang['Stok']:
                print("Stok tidak mencukupi.")
            else:
                barang['Stok'] -= jumlah_stok
        print(f"Stok baru: {barang['Stok']}")
    else:
        print(f"{len(hasil_pencarian)} barang ditemukan:")
        for idx, barang in enumerate(hasil_pencarian):
            print(f"{idx+1}. ", end="")
            tampilkan_data_barang(barang)

        pilihan_stok = input_angka("Masukkan nomor barang yang ingin diubah stok: ", int, 1)
        barang = hasil_pencarian[pilihan_stok - 1]
        tampilkan_data_barang(barang)
        jumlah_stok = input_angka(f"Masukkan jumlah stok {'tambahan' if tipe_aksi == 'restock' else 'terjual'}: ", int, 1)

        if tipe_aksi == 'restock':
            barang['Stok'] += jumlah_stok
        else:
            if jumlah_stok > barang['Stok']:
                print("Stok tidak mencukupi.")
            else:
                barang['Stok'] -= jumlah_stok
        print(f"Stok baru: {barang['Stok']}")

# Fungsi Hapus Barang
def hapus_barang():
    query = input("Masukkan ID/Nama/Kategori/Supplier barang yang akan dihapus: ").lower()
    hasil_pencarian = cari_barang(query)

    if not hasil_pencarian:
        print("Barang tidak ditemukan.\n")
        return

    if len(hasil_pencarian) == 1:
        barang = hasil_pencarian[0]
        tampilkan_data_barang(barang)
        if konfirmasi_aksi("Apakah Anda yakin ingin menghapus barang ini? (ya/tidak): "):
            barang_toko.remove(barang)
            print("Barang berhasil dihapus.\n")
    else:
        print(f"{len(hasil_pencarian)} barang ditemukan:")
        for idx, barang in enumerate(hasil_pencarian):
            print(f"{idx+1}. ", end="")
            tampilkan_data_barang(barang)

        pilihan_hapus = input_angka("Masukkan nomor barang yang ingin dihapus: ", int, 1)
        barang = hasil_pencarian[pilihan_hapus - 1]
        tampilkan_data_barang(barang)
        if konfirmasi_aksi("Apakah Anda yakin ingin menghapus barang ini? (ya/tidak): "):
            barang_toko.remove(barang)
            print("Barang berhasil dihapus.\n")

# Fungsi Lihat Barang Kosong
def lihat_barang_kosong():
    barang_kosong = (barang for barang in barang_toko if barang['Stok'] == 0)
    barang_hampir_habis = [barang for barang in barang_toko if 0 < barang['Stok'] < 5]

    if not barang_kosong and not barang_hampir_habis:
        print("Tidak ada barang yang stoknya habis atau hampir habis.\n")
        return

    if barang_kosong:
        print("Barang yang stoknya habis:")
        for barang in barang_kosong:
            tampilkan_data_barang(barang)
        print("")

    if barang_hampir_habis:
        print("Barang yang stoknya hampir habis:")
        for barang in barang_hampir_habis:
            tampilkan_data_barang(barang)
        print("")

# Fungsi Pencarian Barang berdasarkan ID, Nama, Kategori, atau Supplier secara langsung
def cari_barang_manual():
    query = input("Masukkan Data (ID/Nama/Kategori/Supplier): ").lower()
    hasil = cari_barang(query)

    if hasil:
        print("Hasil Pencarian:")
        for barang in hasil:
            tampilkan_data_barang(barang)
    else:
        print("Barang tidak ditemukan.\n")

# Submenu Manajemen Barang
def submenu_manajemen():
    while True:
        print("=== Submenu Manajemen Barang ===")
        print("1. Tambah Barang")
        print("2. Ubah Barang")
        print("3. Hapus Barang")
        print("4. Restock Barang")
        print("5. Penjualan Barang")
        print("6. Kembali")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            ubah_barang()
        elif pilihan == "3":
            hapus_barang()
        elif pilihan == "4":
            query = input("Masukkan ID/Nama/Kategori/Supplier barang yang akan di-restock: ").lower()
            ubah_stok_barang(query, 'restock')
        elif pilihan == "5":
            query = input("Masukkan ID/Nama/Kategori/Supplier barang yang dijual: ").lower()
            ubah_stok_barang(query, 'penjualan')
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid.\n")

# Submenu Laporan Barang
def submenu_laporan():
    while True:
        print("=== Submenu Laporan Barang ===")
        print("1. Tampilkan Semua Barang")
        print("2. Lihat Barang Kosong")
        print("3. Cari Barang")
        print("4. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            lihat_barang_kosong()
        elif pilihan == "3":
            cari_barang_manual()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.\n")

# Menu Utama dengan submenus yang lebih kompleks
def menu_utama():
    while True:
        print("=== Sistem Manajemen Toko Distributor Alat & Perlengkapan Laundry ===")
        print("1. Manajemen Barang")
        print("2. Laporan Barang")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            submenu_manajemen()  # Panggil submenu manajemen barang
        elif pilihan == "2":
            submenu_laporan()  # Panggil submenu laporan barang
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-3.\n")

# Menjalankan program
if __name__ == "__main__":
    menu_utama()