# kondisional-perulangan
## struktur-kondisi-Latihan1

<p>

### sourcecode

<p>    
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
<p>
    
![screenshot-struktur-kondisi-latihan1](https://user-images.githubusercontent.com/92582081/142558243-de1bce9b-11d7-42d6-a7ef-5e4b52011c88.PNG)
    
<p>
    
## struktur-kondisi-latihan2
    
<p>
    
### sourcecode
    
<p>
<P> print ("------------------")
<P> print ("Pertemuan ke 7")
<P> print ("kondisional-perulangan")
<P> print ("struktur-kondisi-latihan 2")
<P> print ("------------------")
<P> def pengulangan():
<P>     print ("")
<P> a = int(input("input bilangan  1 = "))
<P> b = int(input("input bilangan  2 = "))
<P> c = int(input("input bilangan  3 = "))   
<P> print("----------------")
<P> print("urutan bilangan")
<P> if a>b and a>c :
<P>     if b>c:
<P>         print(a,b,c)
<P>     else:
<P>         print(a,c,b)
<P> elif b>a and b>c:
<P>     if a>c:
<P>         print(b,a,c)
<P>     else:
<P>         print (b,c,a)
<P> else :
<P>     if a>b:
<P>         print(c,a,b)
<P>     else:
<P>         print(c,b,a)
<P>     print("")    

### Screenshot program
    
<p>
    
![screenshot-struktur-kondisi-latihan2](https://user-images.githubusercontent.com/92582081/142562853-64b75e0a-3019-401b-af6b-b81a55553534.PNG)

<p>
 
## Perulangan latihan2
    
<p>
    
### sourcecode
    
<p> print ("------------------")
<p> print ("Pertemuan ke 7")
<p> print ("kondisional-perulangan")
<p> print ("perulangan-latihan 2")
<p> print ("------------------")
<p> jumlah =int(input("masukkan jumlah n :"))
<p> import random
<p> for i in range (jumlah) :
<p>     print("data ke", i+1, "=", (random.uniform(0.1,0.5)))

### Penjelasan program
    
<p> 1. print ('Tampilkan n Bilangan Acak yang Lebih Kecil Dari 0.5') Untuk Menampilkan atau Mencetak kalimat Tampilkan N Bilangan Acak yang Lebih Kecil Dari 0.5
<p> 2. jumlah=int(input("Masukan Jumlah N : ")) Untuk menentukan jumlah input yang di inginkan sesuai tipe data yaitu interger tipe data bilangan bulat import random*
<p> 3. for i in range ( jumlah ) : Untuk Pengulangan dengan range jumlah
<p> 4. print("Data ke", 1+i,"=>", (random.uniform(0.1,0.5))) Untuk menampilkan atau mencetak urutan data sesuai jumlah inputan dengan hasil di bawah 0.5    
    
<p>
    
### Screenshot program
    
<p>  

![screenshot-perulangan-latihan2](https://user-images.githubusercontent.com/92582081/142565586-5f6d3ae5-372f-41dc-9201-f11e7b979f4e.PNG)

