global ad
ad = "deneme2.txt"
def dosyaac():
    sec=input("Dosya oluşturmak istediginize emin misiniz E/H >")
    if(sec == 'E'):
        ad = input('Dosya adını giriniz:')
        ad = ad +'.txt'
        with open(ad,'w') as dosya:
            dosya.close()
    if(sec == 'H'):
        return
def listele():
    with open(ad,'r') as dosya:
        bilgiler = dosya.readlines()
        i = 0
        for bilgi in bilgiler:
            print(i,".",bilgi)
            i+=1
def bilgiekle():
    with open(ad, 'a') as dosya:
        bilgi = []
        bilgi.append(input("Isim Giriniz: "))
        bilgi.append(input("1.Notu Giriniz: "))
        dosya.writelines(bilgi)
def bilgisil():
    with open(ad,'r') as dosya:
        bilgiler=dosya.readlines()
        silinecek = int(input("Silinecek kayıt numarasi: "))
        bilgiler.pop(silinecek)
    with open(ad,'w') as dosya:
        dosya.writelines(bilgiler)

while 1:
    print("""
Dosya olusturmakk icin 1:
Veri silmek icin       2:
Bilgi eklemek icin     3:
Listelemek    icin     4:
Cıkmak        icin     5:

    """)
    secenek = int(input("Bir secenek giriniz:"))
    if (secenek == 1):
        dosyaac()
    if (secenek == 2):
        bilgisil()
    if (secenek == 3):
        bilgiekle()
    if (secenek == 4):
        listele()
    if (secenek == 5):
        exit()
