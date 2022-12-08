# import heapq
# import csv

# login = []
# data = []
# count = 0

# with open ('login.csv') as log:
#     logs = csv.reader(log)
#     for i in logs:
#         login.append(i)

# with open ('database.csv') as db:
#     dbase = csv.reader(db)
#     for i in dbase:
#         data.append(i)

# def Login():
#     global count
#     username = input('Masukkan Username : ')
#     password = input('Masukkan Password : ')

#     for i in range(len(login)-1):
#         if username == login[i][0] and password == login[i][0]:
#             Main()
#         else:
#             print('username atau password salah!\n')
#             count+=1
#             if count < 3:
#                 Login()

# def Register():
#     username = input('Masukkan Username : ')
#     password = input('Masukkan Password : ')
    

# def Main():
#     print('='*40)
#     print("\t\t MENU")
#     print('='*40)
#     print('\t1. Show Data')
#     print('\t2. Insert Data')
#     print('\t3. Delete Data')
#     print('='*40)
#     choice = input('Pilih menu : ')

#     if choice == '1':
#         Show()
#     elif choice == '2':
#         Insert()
#     elif choice == '3':
#         Delete()
#     else:
#         print("Menu tidak valid")

# def Show():
#     print("="*17, "DATA", "="*17)
#     print ("{:<10} {:<15} {:<10} {:<10} {:<10} {:<10}".format('Barang','Tanggal','Pengirim','Penerima', 'Jarak', 'Layanan'))
#     for k, v in data:
#         barang, tanggal, pengirim, penerima, jarak, layanan = v
#         print ("{:<10} {:<15} {:<10} {:<10} {:<10} {:<10}".format(k, barang, tanggal, pengirim, penerima, jarak, layanan))
#     print("="*40)
#     Main()

# def Insert():
#     Main()

# def Delete():
#     Main()

# Login()

d = {1: ["Python", 33.2, 'UP'],
2: ["Java", 23.54, 'DOWN'],
3: ["Ruby", 17.22, 'UP'],
10: ["Lua", 10.55, 'DOWN'],
5: ["Groovy", 9.22, 'DOWN'],
6: ["C", 1.55, 'UP']
}
print ("{:<8} {:<15} {:<10} {:<10}".format('Pos','Lang','Percent','Change'))
for k, v in d.items():
    lang, perc, change = v
    print ("{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change))