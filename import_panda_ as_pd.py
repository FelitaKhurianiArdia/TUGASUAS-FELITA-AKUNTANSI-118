import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('nama_file.csv')

# Menampilkan 5 baris pertama data
print(data.head())

# Info singkat tentang data
print(data.info())

# Statistik deskriptif
print(data.describe())

# Handling missing values
# Misalnya, mengganti nilai yang hilang dengan mean atau median
data['kolom'].fillna(data['kolom'].mean(), inplace=True)

# Membuat plot
plt.figure(figsize=(10, 6))
plt.scatter(data['kolom_x'], data['kolom_y'])
plt.title('Scatter Plot')
plt.xlabel('Kolom X')
plt.ylabel('Kolom Y')
plt.show()

# Menyimpan data setelah preprocessing
data.to_csv('nama_file_preprocessed.csv', index=False)
