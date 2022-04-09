'''
    Muhamad Zein Algifari
    200511125
    R3
    CRUD Postgresql
'''

import psycopg2
import os

DB_NAME = "kampus"
DB_USER = "postgres"
DB_PASS = "zein"
DB_HOST = "123"
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
                CREATE TABLE Customers
                (
                    customer_id serial primary key,
                    name varchar(50) NOT NULL,
                    address varchar(100) NOT NULL
                )
                    """)
    db.commit()
    print("Selamat Anda Telah Berhasil Membuat Tabel...")


# create_table(db)


def show_data(db):
    print("\nRead")
    cursor = db.cursor()
    sql = "SELECT * FROM Customers"
    cursor.execute(sql)
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in cursor:
            print(data)
    print('\n')


def insert_data(db):
    name = input("\nMasukan nama: ")
    address = input("Masukan alamat: ")
    val = (name, address)
    cursor = db.cursor()
    sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("\n{} data berhasil disimpan".format(cursor.rowcount))
    print('\n')


def update_data(db):
    cursor = db.cursor()
    show_data(db)
    customer_id = input("\npilih id customer: ")
    name = input("Nama baru: ")
    address = input("Alamat baru: ")

    sql = "UPDATE Customers SET name=%s, address=%s WHERE customer_id=%s"
    val = (name, address, customer_id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))
    print('\n')


def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    customer_id = input("\npilih id customer: ")
    sql = "DELETE FROM Customers WHERE customer_id=%s"
    val = (customer_id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))
    print('\n')


def search_data(db):
    cursor = db.cursor()
    keyword = input("\nKata kunci (Nama atau Alamat): ")
    sql = "SELECT * FROM Customers WHERE name LIKE %s OR address LIKE %s"
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
