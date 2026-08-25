import random
import time

bank_soal = [
    {
        "soal": "Apa output dari: print(2 + 3 * 4)?",
        "pilihan": ["A. 20", "B. 14", "C. 24", "D. 10"],
        "jawaban": "B",
        "penjelasan": "Perkalian (*) dikerjakan lebih dulu dari penjumlahan (+). Jadi 3*4=12, lalu 2+12=14."
    },
    {
        "soal": "Manakah cara yang benar untuk membuat list di Python?",
        "pilihan": ["A. nama = (1, 2, 3)", "B. nama = {1, 2, 3}", "C. nama = [1, 2, 3]", "D. nama = <1, 2, 3>"],
        "jawaban": "C",
        "penjelasan": "List di Python menggunakan tanda kurung siku [ ]. Kurung biasa () untuk tuple, kurung kurawal {} untuk set/dictionary."
    },
    {
        "soal": "Berapa panjang list ini: buah = ['apel', 'mangga', 'jeruk']?",
        "pilihan": ["A. 2", "B. 4", "C. 3", "D. 0"],
        "jawaban": "C",
        "penjelasan": "Fungsi len() menghitung jumlah elemen. List buah punya 3 elemen: 'apel', 'mangga', 'jeruk'."
    },
    {
        "soal": "Apa yang dilakukan kode ini?\nfor i in range(5):\n    print(i)",
        "pilihan": ["A. Mencetak angka 1 sampai 5", "B. Mencetak angka 0 sampai 4", "C. Mencetak angka 0 sampai 5", "D. Error"],
        "jawaban": "B",
        "penjelasan": "range(5) menghasilkan angka dari 0 sampai 4 (tidak termasuk 5). Jadi output-nya: 0, 1, 2, 3, 4."
    },
    {
        "soal": "Apa output dari kode ini?\nx = 10\nif x > 5:\n    print('Besar')\nelse:\n    print('Kecil')",
        "pilihan": ["A. Kecil", "B. Error", "C. Besar", "D. 10"],
        "jawaban": "C",
        "penjelasan": "x = 10, dan 10 > 5 adalah True, jadi blok if dijalankan dan mencetak 'Besar'."
    },
    {
        "soal": "Bagaimana cara mengakses elemen pertama dari list ini?\nwarna = ['merah', 'biru', 'hijau']",
        "pilihan": ["A. warna[1]", "B. warna[0]", "C. warna[-1]", "D. warna.first()"],
        "jawaban": "B",
        "penjelasan": "Indeks di Python dimulai dari 0. Jadi elemen pertama ada di indeks [0], bukan [1]."
    },
    {
        "soal": "Apa fungsi dari keyword 'def' di Python?",
        "pilihan": ["A. Mendefinisikan variabel", "B. Mendefinisikan fungsi", "C. Mendefinisikan list", "D. Mendefinisikan loop"],
        "jawaban": "B",
        "penjelasan": "'def' adalah singkatan dari 'define' — digunakan untuk membuat/mendefinisikan sebuah fungsi baru."
    },
    {
        "soal": "Apa output dari: print('Python' * 3)?",
        "pilihan": ["A. Error", "B. Python3", "C. PythonPythonPython", "D. 3Python"],
        "jawaban": "C",
        "penjelasan": "Operator * pada string berarti pengulangan. 'Python' * 3 = 'PythonPythonPython'."
    },
    {
        "soal": "Manakah tipe data yang BENAR untuk angka desimal di Python?",
        "pilihan": ["A. int", "B. str", "C. bool", "D. float"],
        "jawaban": "D",
        "penjelasan": "float digunakan untuk angka desimal (seperti 3.14). int untuk bilangan bulat, str untuk teks, bool untuk True/False."
    },
    {
        "soal": "Apa yang dilakukan fungsi input() di Python?",
        "pilihan": ["A. Mencetak teks ke layar", "B. Meminta pengguna memasukkan data", "C. Menyimpan data ke file", "D. Menghitung nilai matematika"],
        "jawaban": "B",
        "penjelasan": "input() digunakan untuk menerima/meminta data dari pengguna melalui keyboard. Hasilnya selalu berupa string."
    }
]

# fungsi fungsi game

def tampilkan_header():
    """Menampilkan header quiz"""
    print("\n" + "=" * 50)
    print("       🐍 PYTHON QUIZ CHALLENGE! 🐍")
    print("=" * 50)
    print("Uji pengetahuan Python-mu di sini!")
    print("Jawab dengan mengetik huruf: A, B, C, atau D")
    print("=" * 50 + "\n")


def tampilkan_soal(nomor, soal_dict, total_soal):
    """Menampilkan satu soal beserta pilihan jawabannya"""
    print(f"📌 Soal {nomor} dari {total_soal}")
    print("-" * 40)
    print(f"{soal_dict['soal']}\n")
    for pilihan in soal_dict['pilihan']:
        print(f"   {pilihan}")
    print()


def minta_jawaban():
    """Meminta jawaban dari pemain dan validasi inputnya"""
    pilihan_valid = ['A', 'B', 'C', 'D']
    while True:
        jawaban = input("Jawaban kamu (A/B/C/D): ").upper().strip()
        if jawaban in pilihan_valid:
            return jawaban
        else:
            print("⚠️  Pilih A, B, C, atau D saja ya!\n")


def cek_jawaban(jawaban_pemain, soal_dict):
    """Mengecek apakah jawaban pemain benar"""
    if jawaban_pemain == soal_dict['jawaban']:
        print("\n✅ BENAR! Kamu hebat!")
        print(f"💡 Penjelasan: {soal_dict['penjelasan']}\n")
        return True
    else:
        print(f"\n❌ Salah! Jawaban yang benar adalah: {soal_dict['jawaban']}")
        print(f"💡 Penjelasan: {soal_dict['penjelasan']}\n")
        return False


def tampilkan_hasil_akhir(skor, total_soal):
    """Menampilkan hasil akhir dan evaluasi pemain"""
    persentase = (skor / total_soal) * 100

    print("\n" + "=" * 50)
    print("           📊 HASIL QUIZ KAMU")
    print("=" * 50)
    print(f"Skor kamu   : {skor} dari {total_soal}")
    print(f"Persentase  : {persentase:.0f}%")

    # evaluasi berdasarkan skor
    if persentase == 100:
        print("Rating      : 🏆 SEMPURNA! Kamu luar biasa!")
        print("Kamu sudah menguasai dasar-dasar Python!")
    elif persentase >= 80:
        print("Rating      : ⭐⭐⭐ EXCELLENT!")
        print("Hampir sempurna — terus semangat belajar!")
    elif persentase >= 60:
        print("Rating      : ⭐⭐ BAGUS!")
        print("Sudah cukup baik, tapi masih bisa lebih baik lagi!")
    elif persentase >= 40:
        print("Rating      : ⭐ TERUS BERLATIH!")
        print("Jangan menyerah — ulangi materinya ya!")
    else:
        print("Rating      : 💪 JANGAN MENYERAH!")
        print("Mulai dari dasar lagi, kamu pasti bisa!")

    print("=" * 50)


def pilih_jumlah_soal():
    """Meminta pemain memilih jumlah soal"""
    print("Mau mengerjakan berapa soal?")
    print("   1. 5 soal (cepat)")
    print("   2. 10 soal (lengkap)")
    while True:
        pilihan = input("\nPilih 1 atau 2: ").strip()
        if pilihan == "1":
            return 5
        elif pilihan == "2":
            return 10
        else:
            print("⚠️  Pilih 1 atau 2 saja ya!")


def main():
    """Fungsi utama yang menjalankan quiz"""
    tampilkan_header()

    # pilih jumlah soal
    jumlah_soal = pilih_jumlah_soal()

    # acak dan ambil soal sesuai jumlah yang dipilih
    soal_terpilih = random.sample(bank_soal, jumlah_soal)

    print(f"\n🚀 Quiz dimulai! {jumlah_soal} soal menantimu!\n")
    time.sleep(1)

    # variabel skor
    skor = 0

    # loop melalui setiap soal
    for nomor, soal in enumerate(soal_terpilih, start=1):
        tampilkan_soal(nomor, soal, jumlah_soal)
        jawaban = minta_jawaban()
        benar = cek_jawaban(jawaban, soal)

        if benar:
            skor += 1

        # jeda sebentar sebelum soal berikutnya
        if nomor < jumlah_soal:
            time.sleep(0.5)
            print("Lanjut ke soal berikutnya...\n")
            print("-" * 40)

    # tampilkan hasil akhir
    tampilkan_hasil_akhir(skor, jumlah_soal)

    # tanya mau main lagi
    print()
    lagi = input("Mau coba lagi? (ya/tidak): ").lower().strip()
    if lagi == "ya":
        main()
    else:
        print("\nTerima kasih sudah bermain! Terus semangat belajar Python! 🐍👋\n")


if __name__ == "__main__":
    main()