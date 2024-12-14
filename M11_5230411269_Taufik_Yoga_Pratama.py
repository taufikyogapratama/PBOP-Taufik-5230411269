# -*- coding: utf-8 -*-
"""Copy of Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HyvprqqF6j0188aa7aK3YQB2ZfX5V8Oo
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

data_sudah_diinput = False


# data_sudah_diinput["Temperature"].fillna(data["Temperature"].median(), inplace=True)
# data_sudah_diinput["Humidity"].fillna(data["Humidity"].median(), inplace=True)
# data_sudah_diinput["PM2.5"].fillna(data["PM2.5"].median(), inplace=True)
# data_sudah_diinput["PM10"].fillna(data["PM10"].median(), inplace=True)
# data_sudah_diinput["NO2"].fillna(data["NO2"].median(), inplace=True)
# data_sudah_diinput["SO2"].fillna(data["SO2"].median(), inplace=True)
# data_sudah_diinput["CO"].fillna(data["CO"].median(), inplace=True)
# data_sudah_diinput["Proximity_to_Industrial_Areas"].fillna(data["Proximity_to_Industrial_Areas"].median(), inplace=True)
# data_sudah_diinput["Population_Density"].fillna(data["Population_Density"].median(), inplace=True)


# data["Air Quality"].fillna(data["Air Quality"].mode()[0], inplace=True)

def pohon_keputusan(data, fitur, target):
  """
  Fungsi untuk mengolah data dengan algoritma pohon keputusan.

  Args:
    data: DataFrame pandas yang berisi data.
    fitur: List nama kolom fitur.
    target: Nama kolom target.

  Returns:
    Akurasi model.
  """
  X = data[fitur]
  y = data[target]
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  model = DecisionTreeClassifier(random_state=42)

  model.fit(X_train, y_train)

  y_pred = model.predict(X_test)

  akurasi = accuracy_score(y_test, y_pred)

  return akurasi

def Jaringan_Syaraf(data, fitur, target):
    """
    Fungsi untuk mengolah data dengan algoritma Multilayer Perceptron (MLP).

    Args:
        data: DataFrame pandas yang berisi data.
        fitur: List nama kolom fitur.
        target: Nama kolom target.

    Returns:
        Akurasi model.
    """
    X = data[fitur]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = MLPClassifier(hidden_layer_sizes=(100, 50),
                        activation='relu',
                        solver='adam',
                        max_iter=200,
                        random_state=42)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    akurasi = accuracy_score(y_test, y_pred)

    return akurasi



def display_data():
  global data_sudah_diinput
  if data_sudah_diinput:
    print(data_sudah_diinput)
  else:
    print("Anda harus menginputkan data terlebih dahulu melalui menu 'Input bahan'.")

def menu_bahan():
  global data_sudah_diinput
  File = input("Masukkan file: ")
  fitur_str = input("Masukkan fitur (pisahkan dengan koma): ")
  algoritma = input("Masukkan algoritma: ")
  fitur = [f.strip() for f in fitur_str.split(',')]
  data_sudah_diinput = True
  return File, fitur, algoritma

def Analisis_data(algoritma, fitur):
  if algoritma == "Pohon Keputusan":
    target = 'Air Quality'
    pohon_keputusan(data_sudah_diinput, fitur, target)
  elif algoritma == "Jaringan Syaraf":
    target = 'Air Quality'
    Jaringan_Syaraf(data_sudah_diinput, fitur, target)

def menu_utama():
  print("========== Menu Utama ==========")
  print("1. Tampilkan Data")
  print("2. Input bahan")
  print("3. Analisis Data")
  print("4. Keluar")
  pilihan = input("Masukkan pilihan: ")
  return pilihan

fitur = []
algoritma = ""

while True:
  pilihan = menu_utama()
  if pilihan == "1":
    display_data()
  elif pilihan == "2":
    print("Hanya ada file air_quality.xlsx")
    print(" ")
    print("fitur fitur: ")
    print("1. Temperature")
    print("1. Humidity")
    print("1. PM2.5")
    print("1. PM10")
    print("1. NO2")
    print("1. SO2")
    print("1. CO")
    print("1. Proximity_to_Industrial_Areas")
    print("1. Population_Density")
    print(" ")
    print("Algoritma: ")
    print("1. Pohon Keputusan")
    print("2. Jaringan Syaraf")
    File, fitur_baru, algoritma = menu_bahan()
    fitur = fitur_baru
    algoritma = algoritma
  elif pilihan == "3":
    print(Analisis_data(algoritma, fitur))
  elif pilihan == "4":
    break
  else:
    print("Pilihan tidak valid")