"""
Pemilik Toko bahan bangunan UD. Subur memesan sebuah program kepada Anda untuk dapat menampilkan
beberapa bahan bangunan yang dijualnya pada komputer. Sehingga konsumen dapat memilih dan membeli
barang dalam jumlah yang diinginkannya dan mengetahui jumlah uang yang harus dibayarnya. Berikut daftar
bahan bangunan yang dijualnya:
a. Asbes Gelombang @ Rp60.000
b. Cat Tembok Dulux 1Galon @ Rp250.000
c. Cat Tembok Avian 1 Galon @ Rp350.000
d. Aquaproof 5 Kg @ Rp50.000
e. Seng 2mm @ Rp70.000
f. Spandeks 1mm @ Rp92.000
Pembeli akan diberikan potongan 5% bila total pembelian sebelum PPN bernilai minimal Rp 500.000
Dari seluruh total pembayaran tersebut akan dikenakan pajak PPN 2%.
"""

harga = [0,60000,250000,350000,50000,70000,92000] # harga barang
namaBarang = [0,"ASBES GELOMBANG","CAT TEMBOK DULUX 1 GALON ","CAT TEMBOK AVIAN 1 GALON","AQUAPROOF 5 KG","SENG 2MM","SPANDEKS 1MM"] #list barang
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
            print("1.ASBES GELOMBANG              @Rp60.000")
            print("2.CAT TEMBOK DULUX 1 GALON     @Rp250.000")
            print("3.CAT TEMBOK AVIAN 1 GALON     @Rp350.000")
            print("4.AQUAPROOF 5 KG               @Rp50.000")
            print("5.SENG 2MM                     @Rp70.000")
            print("6.SPANDEKS 1MM                 @Rp92.000")
            print("=================================================")
            pilihBarang = int(input(">>PILIH LIST BARANG       :"))
            if int(pilihBarang) < 0 or int(pilihBarang) > 6: # cek jika kondisi yang dipilih bukan 1 sampai 6
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
                    if(totalHarga >= 500000) :
                        diskon = totalHarga * 5 / 100
                        totalHarga = totalHarga - diskon
                        print(" MENDAPATKAN DISKON    :",diskon) 

                    print(" TOTAL HARGA SEBELUM PPN   :",totalHarga)
                    ppn = totalHarga * 2 /100
                    print(" PPN                       :",ppn)
                    totalHarga = totalHarga + ppn
                    print(" TOTAL HARGA SESUDAH PPN   :",totalHarga)

                print("=========================================")
                jawabUlang = input(">>MULAI PROGRAM LAGI ? Y/T :")
                if(jawabUlang.lower() == "t"):
                    break
