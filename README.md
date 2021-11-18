# kondisional-perulangan
- Sourcode Latihan 1
<p> print ("------------------")
<p> print ("Pertemuan ke 7")
<p> print ("kondisional-perulangan")
<p> print ("perulangan-latihan 1")
<p> print ("Buat program sederhana dengan input 2 buah bilangan, kemudian")
<p> print ("tentukan bilangan terbesar dari kedua bilangan tersebut")
<p> print ("menggunakan statement if")
<p> print ("------------------")

<p> def main():
    
<p>     # menentukan input user
<p>     a = int(input("masukan bilangan pertama: "))
<p>     b = int(input("masukan bilangan kedua: "))
 
<p>      # Menentukan Nilai Bilangan  dengan if else
<p>     if a > b:
<p>         maks = a
<p>     else:
<p>         maks = b
<p>     # mencetak nilai maksimum
<p>     print('Nilai Terbesar adalah %d' % maks)

<p> if __name__ == '__main__':
<p>     main()
