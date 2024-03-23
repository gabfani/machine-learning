#import time
#start_time = time.time() #untuk ngecek waktu
print("helloo world")
#ini contoh komen
"""ini komen 
panjang"""
#print(time.time() - start_time, "detik") #output waktu

"""untuk compile

phyton -m py_compile namafile.py

"""

#coba isi variable
a=11
b=12
print("nilai a= ", a)
print("nilai b= ", b)
print("a+b= ", a+b)

#input
#data yang masuk otomatis string
data1 = input("masukan data= ")
data2 = int(input("masukan data= ")) #ditambah int dulu
data = bool(int(input("masukan data= "))) #jika tanpa int akan dibaca false karena tanpa inputan

print("data= ",data1, "tipe data= ",type(data1))
print("data= ",data2, "tipe data= ",type(data2))
print("data= ",data, "tipe data= ",type(data))
