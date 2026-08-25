import random


def tampilkan_selamat_datang():
    """Menampilkan pesan pembuka game"""
    print("=" * 40)
    print("   🎮 SELAMAT DATANG DI NUMBER GAME!")
    print("=" * 40)
    print("Aku sedang memikirkan sebuah angka...")
    print("Bisakah kamu menebaknya?\n")

def minta_tebakan(percobaan_ke):
    """Meminta pemain memasukkan tebakan"""
    while True:
        try:
            tebakan = int(input(f"Percobaan ke-{percobaan_ke} → Tebak angkamu: "))
            return tebakan
        except ValueError:
            print("⚠️  Masukkan angka yang valid ya!\n")

def cek_tebakan(tebakan, angka_rahasia):
    """
    Mengecek apakah tebakan benar, terlalu kecil, atau terlalu besar
    Mengembalikan: 'benar', 'terlalu_kecil', atau 'terlalu_besar'
    """
    if tebakan == angka_rahasia:
        return "benar"
    elif tebakan < angka_rahasia:
        return "terlalu_kecil"
    else:
        return "terlalu_besar"

def beri_petunjuk(hasil, tebakan):
    """Memberikan petunjuk kepada pemain"""
    if hasil == "terlalu_kecil":
        print(f"📉 {tebakan} terlalu KECIL! Coba angka yang lebih besar.\n")
    elif hasil == "terlalu_besar":
        print(f"📈 {tebakan} terlalu BESAR! Coba angka yang lebih kecil.\n")

def hitung_bintang(jumlah_percobaan, max_percobaan):
    """Menghitung bintang berdasarkan jumlah percobaan"""
    if jumlah_percobaan <= 3:
        return "⭐⭐⭐ LUAR BIASA!"
    elif jumlah_percobaan <= 6:
        return "⭐⭐ BAGUS!"
    else:
        return "⭐ TETAP SEMANGAT!"

def main():
    """Fungsi utama yang menjalankan game"""

    tampilkan_selamat_datang()

    # Variabel pengaturan game
    angka_minimum = 1
    angka_maksimum = 100
    max_percobaan = 10

    # komputer memilih angka rahasia secara acak
    angka_rahasia = random.randint(angka_minimum, angka_maksimum)

    print(f"Aku sudah memilih angka antara {angka_minimum} sampai {angka_maksimum}.")
    print(f"Kamu punya {max_percobaan} kesempatan untuk menebak!\n")

    # variabel untuk melacak permainan
    jumlah_percobaan = 0
    game_selesai = False

    # loop utama game - terus berjalan sampai menang atau kehabisan kesempatan
    while jumlah_percobaan < max_percobaan and not game_selesai:

        jumlah_percobaan += 1
        sisa_kesempatan = max_percobaan - jumlah_percobaan

        # minta tebakan dari pemain
        tebakan = minta_tebakan(jumlah_percobaan)

        # cek hasil tebakan
        hasil = cek_tebakan(tebakan, angka_rahasia)

        # tampilkan hasil
        if hasil == "benar":
            print("\n" + "=" * 40)
            print("🎉 SELAMAT! Kamu BERHASIL menebak!")
            print(f"Angka rahasia memang {angka_rahasia}!")
            print(f"Kamu berhasil dalam {jumlah_percobaan} percobaan.")
            rating = hitung_bintang(jumlah_percobaan, max_percobaan)
            print(f"Rating kamu: {rating}")
            print("=" * 40)
            game_selesai = True

        else:
            # beri petunjuk
            beri_petunjuk(hasil, tebakan)

            # tampilkan sisa kesempatan
            if sisa_kesempatan > 0:
                print(f"💡 Sisa kesempatan: {sisa_kesempatan}\n")

    # jika pemain kehabisan kesempatan
    if not game_selesai:
        print("\n" + "=" * 40)
        print("😔 Sayang sekali, kamu kehabisan kesempatan!")
        print(f"Angka rahasia adalah: {angka_rahasia}")
        print("Jangan menyerah, coba lagi!")
        print("=" * 40)

    # tanya apakah mau main lagi
    print()
    main_lagi = input("Mau main lagi? (ya/tidak): ").lower()
    if main_lagi == "ya":
        print()
        main()  # panggil ulang fungsi main untuk main lagi
    else:
        print("\nTerima kasih sudah bermain! Sampai jumpa! 👋")

# jalankan game
if __name__ == "__main__":
    main()