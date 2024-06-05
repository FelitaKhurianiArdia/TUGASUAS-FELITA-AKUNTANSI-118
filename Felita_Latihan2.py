import pandas as pd

# Load data
data = pd.read_csv('Data_Felita.csv')

# Tampilkan 5 baris pertama data
print(data.head())

# Tampilkan informasi singkat tentang data
print(data.info())

# Tampilkan statistik deskriptif
print(data.describe())

# Tangani nilai yang hilang pada kolom 'gaji'
data['gaji'].fillna(data['gaji'].mean(), inplace=True)

# Tampilkan data setelah preprocessing
print(data)

# Hitung rata-rata gaji
rata_rata_gaji = data['gaji'].mean()
print(f'Rata-rata gaji: {rata_rata_gaji}')

# Hitung rata-rata usia
rata_rata_usia = data['usia'].mean()
print(f'Rata-rata usia: {rata_rata_usia}')

# Tampilkan karyawan dengan gaji tertinggi
karyawan_gaji_tertinggi = data.loc[data['gaji'].idxmax()]
print(f'Karyawan dengan gaji tertinggi: \n{karyawan_gaji_tertinggi}')

# Tampilkan karyawan dengan usia tertua
karyawan_usia_tertua = data.loc[data['usia'].idxmax()]
print(f'Karyawan dengan usia tertua: \n{karyawan_usia_tertua}')

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Scatter plot hubungan antara usia dan gaji
plt.figure(figsize=(10, 6))
plt.scatter(data['usia'], data['gaji'])
plt.title('Scatter Plot Usia vs Gaji')
plt.xlabel('Usia')
plt.ylabel('Gaji')
plt.show()

# Histogram distribusi usia
plt.figure(figsize=(10, 6))
plt.hist(data['usia'], bins=5, edgecolor='k', alpha=0.7)
plt.title('Histogram Usia')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.show()

# Histogram distribusi gaji
plt.figure(figsize=(10, 6))
plt.hist(data['gaji'], bins=5, edgecolor='k', alpha=0.7)
plt.title('Histogram Gaji')
plt.xlabel('Gaji')
plt.ylabel('Frekuensi')
plt.show()

# Diagram Venn
usia_di_bawah_30 = set(data[data['usia'] < 30]['nama'])
gaji_di_atas_60juta = set(data[data['gaji'] > 60000000]['nama'])
nama_berawalan_J = set(data[data['nama'].str.startswith('J')]['nama'])

plt.figure(figsize=(10, 6))
venn3([usia_di_bawah_30, gaji_di_atas_60juta, nama_berawalan_J], 
      ('Usia < 30', 'Gaji > 60 juta', 'Nama berawalan J'))
plt.title('Diagram Venn Karyawan')
plt.show()
