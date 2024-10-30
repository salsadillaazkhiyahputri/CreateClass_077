class PersegiPanjang:
    
    # Konstruktor untuk inisialisasi objek PersegiPanjang.
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    # Menghitung keliling persegi panjang.
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    # Menghitung luas persegi panjang.
    def luas(self):
        return self.panjang * self.lebar

    # Mengembalikan representasi string dari objek PersegiPanjang.
    def __str__(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"


def main():
    print("=== Program Persegi Panjang ===")
    
    try:
        # Meminta input panjang dan lebar dari pengguna
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))
        
        # Validasi input
        if panjang <= 0 or lebar <= 0:
            print("Panjang dan lebar harus bernilai positif!")
            return

        # Membuat objek PersegiPanjang
        persegi_panjang = PersegiPanjang(panjang, lebar)
        
        # Menampilkan informasi dan hasil perhitungan
        print(persegi_panjang)
        print("Keliling:", persegi_panjang.keliling(), "cm")
        print("Luas:", persegi_panjang.luas(), "cm²")
        
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

# Menjalankan program utama
main()