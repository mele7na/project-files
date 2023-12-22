def menu():
    print ("╔════════════════════════╗")
    print ("║  REHBER PROGRAMI       ║")
    print ("╠════════════════════════╣")
    print ("║  1-Rehber ekle         ║")
    print ("║  2-Kayitlari listele   ║")
    print ("║  3-Kayitlari duzelt    ║")
    print ("║  4-Kayit sil           ║")
    print ("║  5-Kayit ara           ║")
    print ("║  Seçimizini giriniz    ║")
    print ("╚════════════════════════╝")
    secim = input ()
    if secim == "1": 
        rehbereEkle()
        listele()
        menu()
    if secim == "2": 
        listele()
        menu()
    if secim =="4":
        sil()
        menu()
        
    if secim =="5":
        ara()
        menu()
def ara():
    kayit={}
    dosya = open("rehber.txt","r")
    okunan = dosya.readlines()
    print(okunan)
    print("\nSatir satir")
    for a in okunan:
        kayit = a
        print(kayit)
        print(type(kayit))
        
def rehbereEkle():
    dosya  = open("deneme.txt","a")
    ad1    = input("Ad    :      ")
    soyad1 = input("Soyad :      ")
    numara1= input("Numara:      ")
    yazilacak = ad1 +"|"+ soyad1 +"|"+ numara1 +"\n"
    yaz = [ad1,soyad1,numara1]
    yazd = {"ad":ad1,"soyad":soyad1,"numara":numara1}
    print(type(yazd))
    dosya.write(str(yazd)+"\n")
    dosya.write("\n")
    dosya.close()
 
def sil():
    import ast
    kayit = {}
    bulunanNo ="kayit bulunamadi"
    dosya = open("rehber.txt","r")
    okunan = dosya.readlines()
    aranan = input("Sileceginiz kisi adi: ")
    yeniListe =[]
    ydosya = open("rehber.txt","w")
    for a in okunan:
        kayit = ast.literal_eval(a)
        if aranan == kayit["ad"]:
            kb = str(kayit)+ "\n"
            ydosya.write(kb)
    
    
    dosya.close()
    ydosya.close()
def ara():
    import ast
    kayit = {}
    bulunamadiNo ="Kayit bulunamadi"
    dosya =("rehbet.txt","r")
    okunan = dosya.readlines()
##    print(okunan)
##    print("\nSatir satir")
    aranan = input("Aradiginiz kisi: ")
    for a in okunan:
        kayit = ast.literal__eval(a)


    
def listele():
    try:
        dosya = open("rehber.txt","r")
        print("   Rehber Kayıt Listesi ")        
        print("═════════════════════════════")
        a = 1        
        for kayit in dosya.readlines():
            print(a, kayit)
            a += 1
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için Enter'a basın.")
        input()




menu()
