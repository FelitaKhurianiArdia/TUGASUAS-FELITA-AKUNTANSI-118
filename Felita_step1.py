import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membuat data langsung dari string CSV untuk contoh ini
from io import StringIO

data_csv = """id,nama,usia,gaji
1,John,30,50000
2,Alice,25,60000
3,Bob,35,75000
4,Lisa,28,
5,Michael,40,80000"""

# Membaca data dari string CSV
data = pd.read_csv(StringIO(data_csv))

# Menampilkan 5 baris pertama data
print(data.head())

# Info singkat tentang data
print(data.info())

# Statistik deskriptif
print(data.describe())

# Handling missing values
# Mengganti nilai yang hilang dengan mean atau median
data['gaji'].fillna(data['gaji'].mean(), inplace=True)

# Membuat plot
plt.figure(figsize=(10, 6))
plt.scatter(data['usia'], data['gaji'])
plt.title('Scatter Plot Usia vs Gaji')
plt.xlabel('Usia')
plt.ylabel('Gaji')
plt.show()

# Menyimpan data setelah preprocessing
data.to_csv('Data_Felita_preprocessed.csv', index=False)
