"""
Bu Sung Hin seorang pemilik bengkel motor UD. Matahari memesan sebuah program kepada Anda untuk dapat
menampilkan beberapa merek Oli motor yang ada pada komputer. Sehingga konsumen dapat memilih dan
membeli oli dalam jumlah yang diinginkannya dan mengetahui jumlah uang yang harus dibayarnya. Berikut
daftar merk oli motor yang dijualnya:
a. Duration SW20 1L @ Rp53.000
b. Castrol Magnatec 1L @ Rp50.000
c. Federal Supreme XX 1L @ Rp54.000
d. Yamalube 1L @ Rp45.000
e. Shell 1L @ Rp46.000
Pembeli akan diberikan potongan 5% bila total pembelian sebelum PPN bernilai minimal Rp 200.000.
Dari seluruh total pembayaran tersebut akan dikenakan pajak PPN 1%.
"""

harga = [0,53000,50000,54000,45000,46000] # harga barang
namaBarang = [0,"DURATION SW20 1L","CASTROL MAGNATEC 1L","FEDERAL SUPREME XX 1L","YAMALUBE 1 L","SHELL 1L"] #list barang
totalHarga = 0 # deklarasi total harga
listbarang = "=================================================\nLIST BARANG YANG DIBELI \n================================================= \n \n " 
jawabUlang = "y" 
while jawabUlang.lower() == "y" :
    pilihLagi = 'y'
    if(pilihLagi.lower() == "y") :
        kodeSalah = "y"
        while kodeSalah == "y" :
            print("=================================================")
            print("LIST BARANG") 
            print("1.DURATION SW20 1L          @Rp53.000")
            print("2.CASTROL MAGNATEC 1L       @Rp50.000")
            print("3.FEDERAL SUPREME XX 1L     @Rp54.000")
            print("4.YAMALUBE 1 L              @Rp45.000")
            print("5.SHELL 1L                  @Rp46.000")
            print("=================================================")
            pilihBarang = int(input(">>PILIH LIST BARANG       :"))
            if int(pilihBarang) < 0 or int(pilihBarang) > 5: # cek jika kondisi yang dipilih bukan 1 sampai 6
                print("BARANG TIDAK DITEMUKAN !")
            else:
               jumlah = int(input(">>JUMLAH BARANG           :")) 
               listbarang += str(pilihBarang) + "." + namaBarang[pilihBarang] + " Jumlah "+str(jumlah)+ "\n"
               totalHarga += harga[pilihBarang] * jumlah
            print("=================================================")
            kodeSalah = input(">>PILIH BARANG LAGI ? Y/T :")
            if(kodeSalah.lower() == "t"):
                if(totalHarga > 0):
                    print(listbarang)
                    print("=========================================")
                    print(" TOTAL HARGA               :",totalHarga)
                    if(totalHarga >= 200000) :
                        diskon = totalHarga * 5 / 100
                        totalHarga = totalHarga - diskon
                        print(" MENDAPATKAN DISKON    :",diskon) 

                    print(" TOTAL HARGA SEBELUM PPN   :",totalHarga)
                    ppn = totalHarga * 1 /100
                    print(" PPN                       :",ppn)
                    totalHarga = totalHarga + ppn
                    print(" TOTAL HARGA SESUDAH PPN   :",totalHarga)

                print("=========================================")
                jawabUlang = input(">>MULAI PROGRAM LAGI ? Y/T :")
                if(jawabUlang.lower() == "t"):
                    break
