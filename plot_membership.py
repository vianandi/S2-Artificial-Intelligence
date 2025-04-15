import matplotlib.pyplot as plt
import numpy as np
from fuzzy_logic import suhu_membership, cahaya_membership, bising_membership

def plot_membership():
    x_suhu = np.linspace(0, 50, 100)
    x_cahaya = np.linspace(0, 1000, 100)
    x_bising = np.linspace(0, 100, 100)

    suhu_values = [suhu_membership(x) for x in x_suhu]
    cahaya_values = [cahaya_membership(x) for x in x_cahaya]
    bising_values = [bising_membership(x) for x in x_bising]

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(x_suhu, [s[0] for s in suhu_values], label='Dingin', color='blue')
    plt.plot(x_suhu, [s[1] for s in suhu_values], label='Normal', color='green')
    plt.plot(x_suhu, [s[2] for s in suhu_values], label='Panas', color='red')
    plt.title("Keanggotaan Suhu")
    plt.xlabel("Suhu (°C)")
    plt.ylabel("Derajat Keanggotaan")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(x_cahaya, [c[0] for c in cahaya_values], label='Redup', color='blue')
    plt.plot(x_cahaya, [c[1] for c in cahaya_values], label='Sedang', color='green')
    plt.plot(x_cahaya, [c[2] for c in cahaya_values], label='Terang', color='red')
    plt.title("Keanggotaan Pencahayaan")
    plt.xlabel("Pencahayaan (lux)")
    plt.ylabel("Derajat Keanggotaan")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(x_bising, [b[0] for b in bising_values], label='Rendah', color='blue')
    plt.plot(x_bising, [b[1] for b in bising_values], label='Sedang', color='green')
    plt.plot(x_bising, [b[2] for b in bising_values], label='Tinggi', color='red')
    plt.title("Keanggotaan Kebisingan")
    plt.xlabel("Kebisingan (dB)")
    plt.ylabel("Derajat Keanggotaan")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_membership()