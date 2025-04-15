import numpy as np

def suhu_membership(x):
    dingin = np.maximum(0, np.minimum(1, (25 - x) / 10))
    normal = np.maximum(0, np.minimum((x - 20) / 5, (30 - x) / 5))
    panas = np.maximum(0, np.minimum(1, (x - 25) / 10))
    return dingin, normal, panas

def cahaya_membership(x):
    redup = np.maximum(0, np.minimum(1, (400 - x) / 200))
    sedang = np.maximum(0, np.minimum((x - 300) / 200, (700 - x) / 200))
    terang = np.maximum(0, np.minimum(1, (x - 600) / 200))
    return redup, sedang, terang

def bising_membership(x):
    rendah = np.maximum(0, np.minimum(1, (60 - x) / 20))
    sedang = np.maximum(0, np.minimum((x - 50) / 20, (80 - x) / 20))
    tinggi = np.maximum(0, np.minimum(1, (x - 70) / 20))
    return rendah, sedang, tinggi

rules = [
    {"suhu": 0, "cahaya": 0, "bising": 0, "produksi": 148.0},
    {"suhu": 0, "cahaya": 1, "bising": 0, "produksi": 150.9},
    {"suhu": 0, "cahaya": 2, "bising": 0, "produksi": 146.5},
    {"suhu": 0, "cahaya": 0, "bising": 1, "produksi": 143.1},
    {"suhu": 0, "cahaya": 1, "bising": 1, "produksi": 146.53},
    {"suhu": 0, "cahaya": 2, "bising": 1, "produksi": 142.73},
    {"suhu": 0, "cahaya": 0, "bising": 2, "produksi": 136.73},
    {"suhu": 0, "cahaya": 1, "bising": 2, "produksi": 140.77},
    {"suhu": 0, "cahaya": 2, "bising": 2, "produksi": 135.97},
    {"suhu": 1, "cahaya": 0, "bising": 0, "produksi": 149.73},
    {"suhu": 1, "cahaya": 1, "bising": 0, "produksi": 153.27},
    {"suhu": 1, "cahaya": 2, "bising": 0, "produksi": 152.13},
    {"suhu": 1, "cahaya": 0, "bising": 1, "produksi": 148.0},
    {"suhu": 1, "cahaya": 1, "bising": 1, "produksi": 150.63},
    {"suhu": 1, "cahaya": 2, "bising": 1, "produksi": 147.63},
    {"suhu": 1, "cahaya": 0, "bising": 2, "produksi": 141.47},
    {"suhu": 1, "cahaya": 1, "bising": 2, "produksi": 145.67},
    {"suhu": 1, "cahaya": 1, "bising": 2, "produksi": 140.2},
    {"suhu": 2, "cahaya": 0, "bising": 0, "produksi": 142.10},
    {"suhu": 2, "cahaya": 1, "bising": 0, "produksi": 146.53},
    {"suhu": 2, "cahaya": 2, "bising": 0, "produksi": 142.17},
    {"suhu": 2, "cahaya": 0, "bising": 1, "produksi": 138.7},
    {"suhu": 2, "cahaya": 1, "bising": 1, "produksi": 141.4},
    {"suhu": 2, "cahaya": 2, "bising": 1, "produksi": 138.3},
    {"suhu": 2, "cahaya": 0, "bising": 2, "produksi": 133.33},
    {"suhu": 2, "cahaya": 1, "bising": 2, "produksi": 138.33},
    {"suhu": 2, "cahaya": 2, "bising": 2, "produksi": 133.77},
]

def hitung_output(suhu, cahaya, bising):
    total_bobot = 0
    total_nilai = 0

    for rule in rules:
        mu_suhu = suhu[rule["suhu"]]
        mu_cahaya = cahaya[rule["cahaya"]]
        mu_bising = bising[rule["bising"]]

        bobot = min(mu_suhu, mu_cahaya, mu_bising)
        total_bobot += bobot
        total_nilai += bobot * rule["produksi"]

    if total_bobot != 0:
        return total_nilai / total_bobot
    else:
        return 0