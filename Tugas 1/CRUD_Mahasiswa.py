'''
    Muhamad Zein Algifari
    200511125
    R3
    CRUD Postgresql
'''

import psycopg2 as db
import os

con = None
connected = None
cursor = None


def connect():
    global con
    global connected
    global cursor
    try:
        con = db.connect(host='localhost', database='kampus',
                         port=5432, user='zein', password='123')
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor


def disconnect():
    global con
    global connected
    global cursor

    if (connected == True):
        cursor.close()
        con.close()
    else:
        con = None
    connected = False


def tampil():
    print('\n')
    sql = "select * from mahasiswa"
    a = connect()
    a.execute(sql)
    record = a.fetchall()
    print(record)
    print('\n')


def entry():
    global con
    global connected
    global cursor

    xnim = input('\nMasukkan NIM: ')
    xnama = input('Masukkan Nama: ')
    xidfk = input('Masukkan ID Fakultas (1...5): ')
    xidpr = input('Masukkan ID Prodi (1...10): ')
    a = connect()
    sql = "insert into mahasiswa(nim,nama,idfakultas,idprodi)values('" + \
        xnim+"', '"+xnama+"', '"+xidfk+"', '"+xidpr+"')"
    a.execute(sql)
    con.commit()
    print('Entry is done')
    print('\n')


def cari():
    global con
    global connected
    global cursor

    xnim = input('\nMasukkan NIM: ')
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim + "'"
    a.execute(sql)
    con.commit()
    record = a.fetchall()
    print(record)
    print('Search is done')
    print('\n')


def ubah():
    global con
    global connected
    global cursor

    xnim = input('\nMasukkan NIM yang dicari: ')
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim + "'"
    a.execute(sql)
    record = a.fetchall()
    print('Data saat ini: ')
    print(record)
    row = a .rowcount
    if(row == 1):
        print('Silahkan untuk mengubah data...')
        xnama = input('Masukkan Nama: ')
        xidfk = input('Masukkan ID Fakultas (1...5): ')
        xidpr = input('Masukkan ID Prodi (1...10): ')
        a = connect()
        sql = "update mahasiswa set nama ='"+xnama+"', idfakultas ='" + \
            xidfk+"', idprodi ='"+xidpr+"' where nim ='"+xnim+"'"
        a.execute(sql)
        con.commit()
        print('Update is done')
        sql = "select * from mahasiswa where nim ='"+xnim+"'"
        a.execute(sql)
        rec = a.fetchall()
        print('Data setelah diubah: ')
        print(rec)
    else:
        print('Data tidak ditemukan')
    print('\n')


def hapus():
    global con
    global connected
    global cursor

    xnim = input('\nMasukkan NIM yang dicari: ')
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim + "'"
    a.execute(sql)
    record = a.fetchall()
    print('Data saat ini: ')
    print(record)
    row = a .rowcount
    if(row == 1):
        jwb = input('Apakah anda ingin menghapus data? (y/t): ')
        if (jwb.upper() == 'Y'):
            a = connect()
            sql = "delete from mahasiswa where nim ='"+xnim+"'"
            a.execute(sql)
            con.commit()
            print('Delete is done')
        else:
            print('Data gagal dihapus')
    else:
        print('Data tidak ditemukan')
    print('\n')


def show_menu():
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
        entry()
    elif menu == "2":
        tampil()
    elif menu == "3":
        ubah()
    elif menu == "4":
        hapus()
    elif menu == "5":
        cari()
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while (True):
        show_menu()
