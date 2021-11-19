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
<P>     print ("masukkan tiga bilangan yang di inginkan !")
<P> a = int(input("input bilangan  1 = "))
<P> b = int(input("input bilangan  2 = "))
<P> c = int(input("input bilangan  3 = "))   
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
<P> pengulangan() 
<p>
    
![screenshot-struktur-kondisi-latihan2](https://user-images.githubusercontent.com/92582081/142562132-f1db7270-257c-4f0e-ad78-8ed51565ba7c.PNG)

<p>
