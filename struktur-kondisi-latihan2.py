print ("------------------")
print ("Pertemuan ke 7")
print ("kondisional-perulangan")
print ("struktur-kondisi-latihan 2")
print ("------------------")

def pengulangan():
    print ("")
a = int(input("input bilangan  1 = "))
b = int(input("input bilangan  2 = "))
c = int(input("input bilangan  3 = "))

print("----------------")
print("urutan bilangan")
if a>b and a>c :
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b>a and b>c:
    if a>c:
        print(b,a,c)
    else:
        print (b,c,a)
else :
    if a>b:
        print(c,a,b)
    else:
        print(c,b,a)
  
