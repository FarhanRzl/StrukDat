from heapq import *

datas = []

print(datas)

def Insert():
    barang   = input('nama barang : ')
    jarak    = int(input('jarak pengiriman : '))
    pengirim = input('nama pengirim : ')
    penerima = input('nama penerima : ')
    print('')
    print('='*10, 'LAYANAN', '='*10)
    print('| 1. Yakin Esok Sampai      |')
    print('| 2. Super Speed (SS)       |')
    print('| 3. REG (Layanan Reguler)  |')
    print('| 4. Ongkos Kirim Ekonomis  |')
    print('='*29)
    print('')
    layanan  = int(input('Layanan yang dipilih : '))
    heappush(datas, [layanan+jarak, barang, jarak, pengirim, penerima, layanan])
    print('')
    Main()

def Delete():
    barang   = input('nama barang : ')
    

def Show():
    print('')
    print('='*28, 'DATA', '='*28)
    print('| {:<10} {:<7} {:<15} {:<15} {:<7} |'.format('Barang', 'Jarak', 'Pengirim', 'Penerima', 'Layanan'))
    for i in datas:
        priority, barang, jarak, pengirim, penerima, layanan = i
        print('| {:<10} {:<7} {:<15} {:<15} {:<7} |'.format(barang, jarak, pengirim, penerima, layanan, priority))
    print('='*62 + '\n')
    Main()

def Main():
    choice = int(input('Menu Yang Dipilih : '))

    if choice == 1:
        Show()
    
    if choice == 2:
        Insert()

Main()