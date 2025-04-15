import matplotlib.pyplot as plt
from fuzzy_logic import suhu_membership, cahaya_membership, bising_membership, rules, hitung_output

suhu = 30
cahaya = 800
bising = 55

fs = suhu_membership(suhu)
fc = cahaya_membership(cahaya)
fb = bising_membership(bising)

bobot_aturan = []
kontribusi = []

for rule in rules:
    mu_suhu = fs[rule["suhu"]]
    mu_cahaya = fc[rule["cahaya"]]
    mu_bising = fb[rule["bising"]]

    bobot = min(mu_suhu, mu_cahaya, mu_bising)
    nilai = bobot * rule["produksi"]

    bobot_aturan.append(bobot)
    kontribusi.append(nilai)

output_akhir = hitung_output(fs, fc, fb)

plt.figure(figsize=(10, 5))
plt.bar(range(len(rules)), kontribusi, tick_label=[f"R{i+1}" for i in range(len(rules))], color='skyblue')
plt.axhline(output_akhir, color='red', linestyle='--', label=f"Output akhir: {output_akhir:.2f}")
plt.title("Kontribusi Tiap Aturan terhadap Output Produksi")
plt.xlabel("Aturan Fuzzy Sugeno")
plt.ylabel("Nilai (bobot × produksi)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
