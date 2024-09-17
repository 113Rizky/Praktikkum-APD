# Masukkan Nama NIM Pembeli Mobil
nama = input("Masukkan Nama Anda: ")
nim = input("Masukkan NIM Anda: ")

# Masukkan Harga Setiap Mobil
harga_setiap_mobil = int(input("Masukkan Harga Setiap Mobil: "))

# Ketika Membeli Mobil Tesla
diskon_tesla = 17 / 100
total_mobil_tesla = harga_setiap_mobil-int(harga_setiap_mobil*diskon_tesla)
print(f"Mobil Tesla seharga {harga_setiap_mobil} dan mendapatkan diskon 17% menjadi {total_mobil_tesla}")

# Ketika Membeli Mobil Toyota
diskon_toyota = 21 / 100
total_mobil_toyota = harga_setiap_mobil-int(harga_setiap_mobil * diskon_toyota)
print(f"Mobil Toyota seharga {harga_setiap_mobil} dan mendapatkan diskon 21% menjadi {total_mobil_toyota}")

# Ketika Membeli Mobil Hyundai
diskon_hyundai = 23 / 100
total_mobil_hyundai = harga_setiap_mobil-int(harga_setiap_mobil * diskon_hyundai)
print(f"Mobil Hyundai seharga {harga_setiap_mobil} dan mendapatkan diskon 23% menjadi {total_mobil_hyundai}")

# Modulus
modulus_setiap_mobil = harga_setiap_mobil % 7
print(f"Harga setiap mobil dimodulus 7 menjadi {modulus_setiap_mobil}")