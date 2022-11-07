print("============WARTEG============")
pembeli = input("Nama Pembeli : ")
alamat = input("Alamat : ")
no_telp = input("Nomor Telp : ")  
tanggal = input("Tanggal : ")


def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n===============MENU MAKANAN===============")
    print("1. Nasi Uduk - Rp.5000,00")
    print("2. Nasi Pecel - Rp.6000,00")
    print("3. Nasi Campur - Rp.7000,00")
    print("4. Nasi Kuning - Rp.8000,00")
    print("5. Nasi Kucing - Rp.10000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3/4/5 : "))
    porsi = int(input("Berapa Porsi : "))

    if nomor == 1:
        totalmakanan = porsi * 5000
        print(porsi,"Nasi Uduk = Rp.",totalmakanan)
        makan=("Nasi Uduk")
    if nomor == 2:
        totalmakanan = porsi * 6000
        print(porsi,"Nasi Pecel = Rp.",totalmakanan)
        makan=("Nasi Pecel")
    if nomor == 3:
        totalmakanan = porsi * 7000
        print(porsi,"Nasi Campur = Rp.",totalmakanan)
        makan=("Nasi Campur")
    elif nomor == 4:
        totalmakanan = porsi * 8000
        print(porsi,"Nasi Kuning = Rp.",totalmakanan)
        makan=("Nasi Kuning")
    elif nomor == 5:
        totalmakanan = porsi * 10000
        print(porsi,"Nasi Kucing = Rp.",totalmakanan)
        makan=("Nasi Kucing")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        makanan()

def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n===============MENU MINUMAN===============")
    print("1. Es Teh - Rp.3000,00")
    print("2. Teh Hangat - Rp.4000,00")
    print("3. Es Jeruk - Rp.5000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3 : "))
    gelas = int(input("Berapa Gelas : "))

    if nomor == 1:
        totalminuman = gelas * 3000
        print(gelas,"Es teh = Rp.",totalminuman)
        minum=("Es Teh")
    elif nomor == 2:
        totalminuman = porsi * 4000
        print(gelas,"Teh Hangat = Rp.",totalminuman)
        minum=("Teh Hangat")
    elif nomor == 3:
        totalminuman = gelas * 5000
        print(gelas,"Es Jeruk = Rp.",totalminuman)
        minum=("Es Jeruk")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        minuman()

makanan()
minuman()
total_semua = totalmakanan + totalminuman

print("\nTotal yang harus di bayar :",total_semua)
uang = int(input("Uang Tunai Pembeli : Rp."))
kembalian = int(uang - total_semua)
print("Kembalian :", kembalian)

print("\n===============S T R U K===============")
print("Nama\t\t:",pembeli)
print("Alamat\t\t:",alamat)
print("Nomor\t\t:",no_telp)
print("Tanggal\t\t:",tanggal)
print("Beli\t\t",porsi,makan,"(Rp.",totalmakanan,")")
print("Beli\t\t",gelas,minum,"(Rp.",totalminuman,")")
print("Tagihan\t\t:Rp.",total_semua)
print("Dibayar\t\t: Rp.",uang)
print("Kembalian\t: Rp.",kembalian)

print("======================================")
print("======================================")