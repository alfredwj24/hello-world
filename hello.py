# Calculator sederhana di Python

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa dibagi 0!"

print("=== Kalkulator Sederhana ===")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Pilih operasi (1/2/3/4): ")
x = float(input("Masukkan angka pertama: "))
y = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    print("Hasil:", tambah(x, y))
elif pilihan == "2":
    print("Hasil:", kurang(x, y))
elif pilihan == "3":
    print("Hasil:", kali(x, y))
elif pilihan == "4":
    print("Hasil:", bagi(x, y))
else:
    print("Pilihan tidak valid!")
# Program ini menyediakan fungsi dasar kalkulator: tambah, kurang, kali, dan bagi.