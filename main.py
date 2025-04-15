from fuzzy_logic import suhu_membership, cahaya_membership, bising_membership, hitung_output

def salam():
    print("=== Sistem Fuzzy Sugeno: Prediksi Produksi Produk ===\n")

def input_data():
    suhu = float(input("Masukkan suhu (C): "))
    cahaya = float(input("Masukkan pencahayaan (lux): "))
    bising = float(input("Masukkan kebisingan (dB): "))
    return suhu, cahaya, bising

salam()
suhu, cahaya, bising = input_data()

fs = suhu_membership(suhu)
fc = cahaya_membership(cahaya)
fb = bising_membership(bising)

print("\n--- Derajat Keanggotaan ---")
print(f"Suhu: {fs}")
print(f"Pencahayaan: {fc}")
print(f"Kebisingan: {fb}")

produksi = hitung_output(fs, fc, fb)

print(f"\n>>> Output produksi akhir (metode Fuzzy Sugeno): {produksi:.2f}")