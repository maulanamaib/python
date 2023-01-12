# import pandas as pd
# import sklearn.linear_model as lm
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# # Membaca Data
# df = pd.read_excel('data\data_regresi_linear.xlsx','Sheet1')

# # memanggil Fungsi
# lr = lm.LinearRegression()

# x = df.Luas_Tanah.values.reshape(-1,1)
# y = df.Harga_dlm_juta.values.reshape(-1,1)

# lr.fit(x,y)

# # Output
# print("[INFO]")
# print('Intercept : ', lr.intercept_)
# print('Coefisien : ', lr.coef_)
# print("\n[PERSAMAAN]")
# print('jadi persaman yg terbentuk adalah : Y = ', lr.intercept_ , ' + ', lr.coef_, 'X')
# print("\n[PREDIKSI]")
# print('prediksi untuk Luas tanah(X) = 1800  maka nilai Harga dlm juta(Y) = ', lr.predict([[1800]]))

# print("\n[MANUAL]")
# # Evaluasi predict
# df['prediksi_harga_dlm_juta'] = lr.predict(x)

# # Evaluasi Manual
# df['SST']= np.square(df['Harga_dlm_juta'] - df['Harga_dlm_juta'].mean())
# df['SSR']= np.square(df['prediksi_harga_dlm_juta'] - df['Harga_dlm_juta'].mean())
# print('SSR=', df['SSR'].sum())
# print('SST=', df['SST'].sum())
# print('perhitungan scr manual R-square = ', df['SSR'].sum() / df['SST'].sum())


# # Evaluasi Built in Function
# print('R-Squared dengan fungsi : ', r2_score(df.Harga_dlm_juta, df.prediksi_harga_dlm_juta))
# print('Mean Absolute Error : ', mean_absolute_error(df.Harga_dlm_juta, df.prediksi_harga_dlm_juta))
# print('Root Mean Squared Error : ', np.sqrt(mean_squared_error(df.Harga_dlm_juta, df.prediksi_harga_dlm_juta)))

# # Grafik
# plt.scatter(x, y, color = 'black')
# plt.plot(x, lr.predict(x), color = 'blue', linewidth = 3)
# plt.title('Luas Tanah vs Harga dlm juta')
# plt.ylabel('Harga_dlm_juta')
# plt.xlabel('Luas_Tanah')
# plt.show()
buku = []


# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print ("[%d] %s" % (indeks, buku[indeks]))


# fungsi untuk menambah data
def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = input("Inputkan ID buku: ")
    if(indeks > len(buku)):
        print ("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

# fungsi untuk menhapus data
def delete_data():
    show_data()
    indeks = input("Inputkan ID buku: ")
    if(indeks > len(buku)):
        print ("ID salah")
    else:
        buku.remove(buku[indeks])

# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    
    menu = input("PILIH MENU> ")
    print("/n")


    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print ("Salah pilih!")


if __name__ == "__main__":

    while(True):
        show_menu()
