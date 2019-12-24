with open('deneme2.txt','r+') as dosya:
    #data = dosya.read()
    #dosya.seek(12)#12 karakter ilerle anlamina geliyor.ve sonrasini al
    #print(dosya.read(5)) #gelen veridende 5 karakteri al diyebiliriz
    #dosya icinde gezinme islemleri yapabilriz.
    #dosya.seek(5)#dosyanın en basindan 5 gider kaldıgı yerde devam etmez
    #dosyaları paketlere çevirip aktarma örnegi yapabilrisin.
    #dosya.seek(0)#en basina ekleme yapmaz üzerine yazma islemi gerceklestirir.
    #data = "Deneme = Deneme\n" + data #dosyanın en basina ekleme yapmak icin uygun yontem.
    #dosya .write(data)
    data = dosya.readlines()#aralara veri eklemek icin listeleri kullanicagiz o yüzden verimizi once listeye ceviriyoruz
    data.insert(1,"Deneme = Deneme\n")
    dosya.seek(0)
    dosya.writelines(data)


