import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv("data_serangan_siber.csv")

# Visualisasi data
plt.figure(figsize=(10,6))
plt.bar(data['tahun'], data['jumlah_serangan'], color='blue')
plt.title('Tren Serangan Siber Berdasarkan Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Serangan')
plt.show()
# Misalkan data sudah berisi beberapa jenis serangan
data_pivot = data.pivot(index='tahun', columns='jenis_serangan', values='jumlah_serangan')

# Visualisasi Stacked Bar Chart
data_pivot.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title('Perbandingan Jenis Serangan Siber Berdasarkan Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Serangan')
plt.show()
