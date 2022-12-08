import heapq
import csv
import os 
import time

login = []
data = []
count = 0

with open ('login.csv') as log:
    logs = csv.reader(log)
    for i in logs:
        login.append(i)

with open ('database.csv') as db:
    dbase = csv.reader(db)
    for i in dbase:
        data.append(i)

def Login():
    global count
    username = input('Masukkan Username : ')
    password = input('Masukkan Password : ')
    time.sleep(5)
    os.system('cls')

    for i in range(len(login)-1):
        if username == login[i][0] and password == login[i][0]:
            Main()
        else:
            print('username atau password salah!\n')
            count+=1
            if count < 3:
                Login()

def Register():
    username = input('Masukkan Username : ')
    password = input('Masukkan Password : ')

    data.append([username, password])

    with open('database.csv', 'w') as dt:
        dts = csv.writer(dt)
        dts.writerows(data)

def Main():
    print('='*40)
    print("\t\t MENU")
    print('='*40)
    print('\t1. Show Data')
    print('\t2. Insert Data')
    print('\t3. Delete Data')
    print('='*40)
    choice = input('Pilih menu : ')

    if choice == '1':
        Show()
    elif choice == '2':
        Insert()
    elif choice == '3':
        Delete()
    else:
        print("Menu tidak valid")

def Show():
    print("="*32, "DATA", "="*32)
    print ("{:<16} {:<15} {:<15} {:<10} {:<8} {:<10}".format('Barang','Tanggal','Pengirim','Penerima', 'Jarak', 'Layanan'))
    for i in range(len(data)-1):
        print ("{:<13} {:<15} {:<15} {:<13} {:<10} {:<10}".format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
    print("="*70)
    Main()

def Insert():
    item = input('Data yang dimasukkan : ')
    heapq.heappush(data, item)
    Main()

def Delete():
    item = input('Data yang dihapus : ')
    heapq.heappop(data)
    Main()

Login()