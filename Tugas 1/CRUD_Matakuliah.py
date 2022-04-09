'''
    Muhamad Zein Algifari
    200511125
    R3
    CRUD Postgresql
'''

import psycopg2
import os

DB_NAME = "kampus"
DB_USER = "zein"
DB_PASS = "123"
DB_HOST = "localhost"
DB_PORT = "5432"
try:
    db = psycopg2.connect(database=DB_NAME, user=DB_USER,
                          password=DB_PASS, host=DB_HOST, port=DB_PORT)
    print("\nServer Telah Terkoneksi Di Database\n")
except:
    print("\nServer Belum Terkoneksi Di Database\n")
cur = db.cursor()


def create_table(db):
    cur.execute("""
                CREATE TABLE Matakuliah
                (
                    idmk serial primary key,
                    kodemk varchar(10) NOT NULL,
                    namamk varchar(50) NOT NULL,
                    sks integer NOT NULL,
                    kode_prodi varchar(10) NOT NULL
                )
                    """)
    db.commit()
    print("Selamat Anda Telah Berhasil Membuat Tabel...")


# create_table(db)


def show_data(db):
    print("\nRead")
    cursor = db.cursor()
    sql = "SELECT * FROM Matakuliah"
    cursor.execute(sql)
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in cursor:
            print(data)
    print('\n')


def insert_data(db):
    kodemk = input("\nMasukan Kode Matakuliah: ")
    namamk = input("Masukan Nama Matakuliah: ")
    sks = input("Masukan jumlah SKS: ")
    prodi = input("Masukan Nama Program Studi: ")

    val = (kodemk, namamk, sks, prodi)
    cursor = db.cursor()
    sql = "INSERT INTO Matakuliah (kodemk, namamk, sks, kode_prodi) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("\n{} data berhasil disimpan".format(cursor.rowcount))
    print('\n')


def update_data(db):
    cursor = db.cursor()
    show_data(db)
    idmk = input("\nPilih id Matakuliah: ")
    kodemk = input("Masukan Kode Matakuliah: ")
    namamk = input("Masukan Nama Matakuliah: ")
    sks = input("Masukan jumlah SKS: ")
    prodi = input("Masukan Nama Program Studi: ")

    sql = "UPDATE Matakuliah SET kodemk =%s, namamk=%s, sks=%s, kode_prodi=%s WHERE idmk=%s"
    val = (kodemk, namamk, sks, prodi, idmk)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))
    print('\n')


def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    idmk = input("\nPilih id Matakuliah: ")
    sql = "DELETE FROM Matakuliah WHERE idmk=%s"
    val = (idmk)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))
    print('\n')


def search_data(db):
    cursor = db.cursor()
    keyword = input("\nKata kunci (Kode Matakuliah atau Nama Matakuliah): ")
    sql = "SELECT * FROM Matakuliah WHERE kodemk LIKE %s OR namamk LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
    print('\n')


def show_menu(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("=================================")
    menu = input("Pilih menu ketik nomor berapa?: ")

    # clear screen
    os.system("cls")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while (True):
        show_menu(db)
