print ("------------------")
print ("Pertemuan ke 7")
print ("kondisional-perulangan")
print ("perulangan-latihan 1")
print ("Buat program sederhana dengan input 2 buah bilangan, kemudian")
print ("tentukan bilangan terbesar dari kedua bilangan tersebut")
print ("menggunakan statement if")
print ("------------------")

def main():
    
    # menentukan input user
    a = int(input("masukkan bilangan pertama: "))
    b = int(input("masukkan bilangan kedua: "))
 
     # Menentukan Nilai Bilangan  dengan if else
    if a > b:
        maks = a
    else:
        maks = b
    # mencetak nilai maksimum
    print ("-------------")
    print('Nilai Terbesar adalah %d' % maks)

if __name__ == '__main__':
    main()