#dosya = open("deneme.txt",w) #dosyaya yazma islemi gerçekleştirmek icin
#dosya = open("deneme.txt",r) #dosyayı okuma islemi gerçekleştirmek içib
#dosya = open("deneme.txt","a") #dosyaya ekleme yapmak icin
#dosya.write("Merhaba Dunya") #dosya icine yazdırmak icin
#read() #readline() # readlines()

dosya = open("deneme.txt","r")
#print(dosya.read()) #dosya icerigini okumamıza yarar.
#print(dosya.readlines()) #bütün satırları alıp listeye cevirir.
liste = dosya.readlines()
print(liste[0])

dosya.close() #bufferda yer kaplamaması iicn
